import os
from google.colab import drive
drive.mount('/content/drive')
os.environ["JAVA_HOME"] =  "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.1.2-bin-hadoop3.2"
import findspark
findspark.init()
from pyspark.sql import SparkSession
sc = SparkSession.builder.master("local[*]").getOrCreate()
lines = sc.sparkContext.textFile('drive/MyDrive/pyspark/text.txt').flatMap(lambda line: line.split(" "))
lines.collect()
wordCounts = lines.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
wordCounts.saveAsTextFile("drive/MyDrive/pyspark/output/")
