# Databricks notebook source
# Databricks notebook source
storageAccountName = "sahrms"
storageAccountAccessKey = dbutils.secrets.get('hrms-kv-scope', 'sahrms-access-key')
mountPoints=["gold","silver","bronze","landing","config"]
for mountPoint in mountPoints:
    if not any(mount.mountPoint == f"/mnt/{mountPoint}" for mount in dbutils.fs.mounts()):
        try:
            dbutils.fs.mount(
            source = "wasbs://{}@{}.blob.core.windows.net".format(mountPoint, storageAccountName),
            mount_point = f"/mnt/{mountPoint}",
            extra_configs = {'fs.azure.account.key.' + storageAccountName + '.blob.core.windows.net': storageAccountAccessKey}
            )
            print(f"{mountPoint} mount succeeded!")
        except Exception as e:
            print("mount exception", e)

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

spark.conf.set(
  "fs.azure.account.key.sahrms.blob.core.windows.net",
  "KMbYMQXzdJpTZ6smJ6HZmLFAPmxH2SiDXr+Bz7NzUw0o+Xl3T6yrtecwmb8c+bIsD4lndl1+dacu+AStygegeA=="
)

# COMMAND ----------

dbutils.fs.ls("wasbs://bronze@sahrms.blob.core.windows.net/")

# COMMAND ----------

dbutils.fs.ls("/mnt/bronze")