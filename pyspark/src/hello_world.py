from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("hello-world")
    .master("local[*]")
    .getOrCreate()
)  # Use n cores in machine

print(spark.version)
