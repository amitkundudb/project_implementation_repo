# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

df=spark.read.json("/FileStore/test_data.json")
schema = spark.read.json(df.rdd.map(lambda row: row["orderDetails"])).schema

df = df.withColumn("orderDetails", from_json("orderDetails", schema)).select(col('*'), col('orderDetails.*')).drop("orderDetails")
df.display()

# COMMAND ----------

p_key = df.select("clientProfileData")
# u_key = df.distinct()
# print(p_key.count())
# print(u_key.count())
p_key.display()

# COMMAND ----------

df.printSchema()

# COMMAND ----------


