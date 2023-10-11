

from pyspark.sql import SparkSession
import pandas as pd
import json
from pyspark.sql.functions import explode
from pyspark.sql.types import *
from pyspark.sql.functions import *



spark = SparkSession.builder.master("local").appName("test").getOrCreate()

#source = spark.read.json(r'/Users/harish/Downloads/dwsample1-json.json')

# Read multiline json file
# multiline_df = spark.read.option("multiline","True") \
#       .json(r'/Users/harish/Downloads/dwsample1-json.json')
# multiline_df.show(10)
#
# print(multiline_df.count())

#source.show()

source = spark.read.option("multiline", "True").\
    json(r"/Users/harish/Downloads/sample2.json")

source.show()

df= source
#df = df.withColumn("phoneNumbers", explode_outer("phoneNumbers"))

df.show()

#df.select(df.address).show()

#df.select(df.age,explode(df.phonenumbers)).show(truncate=False)




# Flatten array of structs and structs
def flatten(df):
    # compute Complex Fields (Lists and Structs) in Schema
    complex_fields = dict([(field.name, field.dataType)
                           for field in df.schema.fields
                           if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    print(complex_fields)
    while len(complex_fields) != 0:
        col_name = list(complex_fields.keys())[0]
        print(col_name)
        print("Processing :" + col_name + " Type : " + str(type(complex_fields[col_name])))

        # if StructType then convert all sub element to columns.
        # i.e. flatten structs
        if (type(complex_fields[col_name]) == StructType):
            expanded = [col(col_name + '.' + k).alias(col_name + '_' + k) for k in
                        [n.name for n in complex_fields[col_name]]]
            df = df.select("*", *expanded).drop(col_name)

        # if ArrayType then add the Array Elements as Rows using the explode function
        # i.e. explode Arrays
        elif (type(complex_fields[col_name]) == ArrayType):
            df = df.withColumn(col_name, explode_outer(col_name))

        # recompute remaining Complex Fields in Schema
        complex_fields = dict([(field.name, field.dataType)
                               for field in df.schema.fields
                               if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
    return df

df = flatten(df)

df.show()

# source.select("address.streetAddress",source.address.streetAddress,\
#               source.address.city,\
#               source.address.state).show()
