# Databricks notebook source
# MAGIC
# MAGIC %sql
# MAGIC  CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.audit;
# MAGIC  CREATE TABLE IF NOT EXISTS tt_hc_adb_ws.audit.load_logs (
# MAGIC  data_source STRING,
# MAGIC  tablename STRING,
# MAGIC  numberofrowscopied INT,
# MAGIC  watermarkcolumnname STRING,
# MAGIC  loaddate TIMESTAMP )
# MAGIC  

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC TRUNCATE TABLE tt_hc_adb_ws.audit.load_logs

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tt_hc_adb_ws.audit.load_logs