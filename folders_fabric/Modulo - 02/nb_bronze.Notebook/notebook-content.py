# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "995d17b5-d671-4ff5-82a2-e29d543a07bb",
# META       "default_lakehouse_name": "lh_bronze",
# META       "default_lakehouse_workspace_id": "8fdbf08f-bdcd-465b-8c6b-ef7e9c798d84",
# META       "known_lakehouses": [
# META         {
# META           "id": "995d17b5-d671-4ff5-82a2-e29d543a07bb"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

mssparkutils.session.stop()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Configurações da Sessão Spark
spark.conf.set("spark.sql.caseSensitive",True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Obtenção do workspace id e do workspace name
import sempy.fabric as fabric
workspace_id = fabric.get_workspace_id()
workspace_name = fabric.resolve_workspace_name()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# PARAMETERS CELL ********************

# Parâmetros passados pelo Pipeline (obtidos a partir do Orquestrador)

# Variáveis Source
source_storage = ""
source_folder = ""
source_file = ""

# Variáveis Target
target_storage = ""
target_table = ""
target_mode = ""

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Caminho absoluto para a origem ( arquivos Parquet )
path_staging = (
    f"abfss://{workspace_name}@onelake.dfs.fabric.microsoft.com/"
    f"{source_storage}.Lakehouse/Files/{source_folder}/{source_file}"
)

# Caminho absoluto para o destino ( tabelas Delta)
path_bronze = (
    f"abfss://{workspace_name}@onelake.dfs.fabric.microsoft.com/"
    f"{target_storage}.Lakehouse/Tables/{target_table}"
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Leitura do arquivo Parquet na Staging
df = spark.read.parquet( path_staging )

# Escrita da tabela Delta na camada Bronze
df.write.format("delta").mode(target_mode).save(path_bronze)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
