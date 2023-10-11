

from pyspark.sql import SparkSession
import pandas as pd
import json


spark = SparkSession.builder.master("local").appName("test").getOrCreate()

source = spark.read.json(r'/Users/harish/Downloads/sample2.json')

source.show()
