
from pyspark.sql import SparkSession
import pandas as pd
import json


spark = SparkSession.builder.master("local").appName("test").getOrCreate()

data = [(2,"sreeni"), (3,"Hari"),(4,'Chandan')]

df = spark.createDataFrame(data=data, schema=['id','name'])

df.write.json("/Users/harish/PycharmProjects/AutomationSept2/Output/json_file")