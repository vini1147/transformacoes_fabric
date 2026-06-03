CREATE   PROCEDURE [SalesLT].[sp.upsert_Address]
    @ModifiedSince DATETIME2(0)
AS
BEGIN
        -- 1. UPDATE (Atualiza linhas existentes)
    UPDATE t
    SET
        t.AddressLine1 = s.AddressLine1,
        t.AddressLine2 = s.AddressLine2,
        t.City = s.City,
        t.StateProvince = s.StateProvince,
        t.CountryRegion = s.CountryRegion,
        t.PostalCode = s.PostalCode,
        t.rowguid = s.rowguid,
        t.ModifiedDate = s.ModifiedDate
    FROM [dw_transformacoes_fabric].[SalesLT].[Address] AS t -- target
    JOIN [lh_transformacoes_fabric].[dbo].[Address] AS s -- source
        ON t.AddressID = s.AddressID
    WHERE s.ModifiedDate >= @ModifiedSince;

    -- 2. INSERT (Adiciona novas linhas)
    INSERT INTO [dw_transformacoes_fabric].[SalesLT].[Address] (
        AddressID,
        AddressLine1,
        AddressLine2,
        City,
        StateProvince,
        CountryRegion,
        PostalCode,
        rowguid,
        ModifiedDate
    )
    SELECT
        s.AddressID,
        s.AddressLine1,
        s.AddressLine2,
        s.City,
        s.StateProvince,
        s.CountryRegion,
        s.PostalCode,
        s.rowguid,
        s.ModifiedDate
    FROM [lh_transformacoes_fabric].[dbo].[Address] AS s
    LEFT JOIN [dw_transformacoes_fabric].[SalesLT].[Address] AS t
        ON t.AddressID = s.AddressID
    WHERE t.AddressID IS NULL

END;