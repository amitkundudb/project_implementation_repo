# Databricks notebook source
from pyspark.sql.types import *

# Define the country schema
country_schema = StructType([
    StructField("type", StringType(), True),
    StructField("enum", ArrayType(StringType(),True), True)
])

# Define the data schema
date_schema = StructType([
        StructField("type", StringType(), True),
        StructField("format", StringType(), True)
    ])

# Define the details schema
data_schema = StructType([
    StructField("type", StringType(), True),
    StructField("properties", ArrayType(StructType([
        StructField("field1", StringType(), True),
        StructField("field2", DoubleType(), True),
        StructField("field3", BooleanType(), True)
    ])), True),
    StructField("required", ArrayType(StringType(),True), True)
])

# Define the issues schema
issues_schema = StructType([
        StructField("type", StringType(), True),
        StructField("properties", ArrayType(StructType([
            StructField("dateFormatIssue", BooleanType(), True),
            StructField("countryDataIssue", BooleanType(), True)
        ])), True)
    ])

# COMMAND ----------

# Define the properties schema
properties_schema_inside = StructType([
    StructField("country", ArrayType(country_schema), True),
    StructField("date", ArrayType(date_schema), True),
    StructField("data", ArrayType(data_schema), True),
    StructField("issues", ArrayType(issues_schema), True)
])

# Define the items schema
items_schema =  StructType([
        StructField("type", StringType(), True),
        StructField("properties", ArrayType(properties_schema_inside), True),
        StructField("required", ArrayType(StringType()), True)
    ])

# COMMAND ----------

# Define the trainingData schema
training_data_schema = StructType([
        StructField("type", StringType(), True),
        StructField("items", ArrayType(items_schema), True)])

# Define the metadata schema
metadata_schema = StructType([
    StructField("type", StringType(), True),
    StructField("properties", StructType([
        StructField("createdBy", StringType(), True),
        StructField("createdAt", StringType(), True),
        StructField("version", StringType(), True)
    ]), True)
])


# COMMAND ----------

schema = StructType([
    StructField("type", StringType(), True),
    StructField("properties", StructType([
        StructField("trainingData",(items_schema), True),
        StructField("metadata", (metadata_schema), True)
    ]), True),
    StructField("required", StringType(), True)
])

# COMMAND ----------

data = "/FileStore/new/sample_json_3__1_.json"

df = spark.read.json(data,multiLine=True,schema=schema)
df.display()
