from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "test-topic") \
    .load()

messages = df.selectExpr("CAST(value AS STRING)")

query = messages.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
# This code sets up a Spark Structured Streaming job that reads messages from a Kafka topic named "test-topic" and 
# prints them to the console. It connects to a Kafka broker running at "kafka:290