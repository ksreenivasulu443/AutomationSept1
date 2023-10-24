#from Utility_functions.Common_libraries import * #get_dataset, count_validation,read_file, read_cosmos, read_db, duplicate


from pyspark.sql import SparkSession
import pandas as pd
import json

jar_path='/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/sqljdbc4-2.0.jar'
spark = SparkSession.builder.master("local")\
    .appName("test") \
    .config("spark.jars","/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/mssql-jdbc-12.2.0.jre8.jar")\
    .config("spark.driver.extraClassPath","/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/mssql-jdbc-12.2.0.jre8.jar") \
    .config("spark.executor.extraClassPath","/Users/harish/Downloads/spark-3.4.1-bin-hadoop3/jars/mssql-jdbc-12.2.0.jre8.jar") \
    .getOrCreate()



server ="sqldatabasedemo100.database.windows.net"
username ='katsreen100'
password='Dharmavaram1@'
database="sampledb"
query="select * from SampleDB.SalesLT.Customer"

#jdbc:sqlserver://;serverName=sqldatabasedemo100.database.windows.net;databaseName=sampledb


def read_db(spark, server, database, username, password, query):
    mssql_df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:sqlserver://;serverName=sqldatabasedemo100.database.windows.net;databaseName=sampledb") \
        .option("query", query) \
        .option("user", username) \
        .option("password", password) \
        .option("driver",'com.microsoft.sqlserver.jdbc.SQLServerDriver')\
        .load()
    return mssql_df

df= read_db(spark, server, database, username, password, query)

df.show()