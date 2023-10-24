

from pyspark.sql import SparkSession
import pandas as pd
import json
from pyspark.sql.functions import explode
from pyspark.sql.types import *
from pyspark.sql.functions import *



spark = SparkSession.builder.master("local").appName("test").getOrCreate()

