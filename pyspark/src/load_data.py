from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col
from pyspark.sql.types import *

spark = (
    SparkSession.builder.appName("load-csv")
    .master("local[*]")
    .config("spark.api.mode", "jvm")
    .getOrCreate()
)

df = spark.read.csv("../data/stocks.csv", header=True, inferSchema=True)

df.show()
df.printSchema()

print(df.Close)
print(df["Date"])

print(col("Date"))

df.select(df.Close, df.Close, df.Close)

df.select("Date", "Close", "Open").show()

date_as_string = df["Date"].cast(StringType()).alias("str_date")
# df["str_date"] = df["Date"].cast(StringType()).alias("str_date")
df = df.withColumn("str_date", df["Date"].cast(StringType()))
df = df.withColumn("rounded_open", F.round(df["Open"], 5)).withColumn(
    "rounded_close", F.round(df["Close"], 5)
)

# df.select(
#     F.format_number("Open", 4).alias("Open"),
#     F.format_number("Close", 4).alias("Close"),
# ).show(truncate=False)


# df = df.withColumn(
#     "Open", F.round(F.col("Open").cast(DecimalType(20, 4)), 4)
# ).withColumn("Close", F.round(F.col("Close").cast(DecimalType(20, 4)), 4))


df.select(df["Date"], date_as_string).show(5)

df.show(5)
