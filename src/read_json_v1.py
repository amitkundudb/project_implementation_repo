# Databricks notebook source
data = '/FileStore/test_data.json'

# COMMAND ----------

df = spark.read.json(data,multiLine=True)
df.display()

# COMMAND ----------

from pyspark.sql.functions import from_json
from pyspark.sql.types import *
map1=MapType(StringType(), StringType())

df3 = df.withColumn("orderDetails", from_json(df["orderDetails"],map1))
df3.printSchema()

# COMMAND ----------

df3.printSchema()

# COMMAND ----------

df3.display()

# COMMAND ----------


