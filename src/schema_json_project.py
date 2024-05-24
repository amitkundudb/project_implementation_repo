# Databricks notebook source
from pyspark.sql.types import *

# COMMAND ----------

parent_schema = StructType([
    StructField("orderId",StringType(),True),
    StructField("sequence",IntegerType(),True),
    StructField("marketplaceOrderId",StringType(),True),
    StructField("marketplaceServicesEndpoint",StringType(),True),
    StructField("sellerOrderId",StringType(),True),
    StructField("origin",StringType(),True),
    StructField("affiliateId",StringType(),True),
    StructField("salesChannel",StringType(),True),
    StructField("merchantName",StringType(),True),
    StructField("workflowIsInError",StringType(),True),
    StructField("statusDescription",StringType(),True),
    StructField("value",StringType(),True),
    StructField("creationDate",StringType(),True),
    StructField("lastChange",StringType(),True),
    StructField("orderGroup",StringType(),True),
    StructField("totals",ArrayType(.....),True),
    StructField("items",ArrayType(.....),True),
    StructField("marketplaceItems",ArrayType(StringType()),True),
    StructField("clientProfileData",ArrayType(.....),True),
    StructField("giftRegistryData",StringType(),True),
    StructField("marketingData",ArrayType(.....),True),
    StructField("ratesAndBenefitsData",ArrayType(.....),True),
    StructField("shippingData",ArrayType(.....),True),
    StructField("paymentData",ArrayType(.....),True),
    StructField("packageAttachment",ArrayType(.....),True),
    StructField("sellers",StructType(
        StructField("id",StringType(),True),
        StructField("name",StringType(),True),
        StructField("logo",StringType(),True),
        StructField("fulfillmentEndpoint",StringType(),True)        
    ),True),
    StructField("callCenterOperatorData",StringType(),True),
    StructField("followUpEmail",StringType(),True),
    StructField("lastMessage",StringType(),True),
    StructField("hostname",StringType(),True),
    StructField("invoiceData",StringType(),True),
    StructField("changesAttachment",StringType(),True),
    StructField("openTextField",StringType(),True),
    StructField("roundingError",IntegerType(),True),
    StructField("orderFormId",StringType(),True),
    StructField("commercialConditionData",StringType(),True),
    StructField("isCompleted",BooleanType(),True),
    StructField("customData",StringType(),True),
    StructField("storePreferencesData",ArrayType(....),True),
    StructField("allowCancellation",BooleanType(),True),
    StructField("allowEdition",BooleanType(),True),
    StructField("isCheckedIn",BooleanType(),True),
    StructField("marketplace",ArrayType(....),True),
    StructField("authorizedDate",TimestampType(),True),
    StructField("invoicedDate",StringType(),True),
    StructField("cancelReason",StringType(),True),
    StructField("itemMetadata",ArrayType(....),True),
    StructField("subscriptionData",StringType(),True),
    StructField("taxData",StringType(),True),
    StructField("checkedInPickupPointId",StringType(),True),
    StructField("cancellationData",StringType(),True),
    StructField("clientPreferencesData",ArrayType(.....),True)
])

# COMMAND ----------


