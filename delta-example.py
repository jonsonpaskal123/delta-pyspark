import pyspark
from delta import configure_spark_with_delta_pip

# ایجاد یک SparkSession با پشتیبانی از Delta Lake
builder = pyspark.sql.SparkSession.builder.appName("DeltaExample") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# مسیر فایل JSON ورودی
input_json_path = "network_traffic_data.json"

# مسیر ذخیره دلتا
delta_table_path = "./delta-table"

# خواندن فایل JSON
df = spark.read.json(input_json_path)

# ذخیره داده‌ها به فرمت دلتا
df.write.format("delta").mode("overwrite").save(delta_table_path)

# خواندن داده‌ها از دلتا برای اطمینان
delta_df = spark.read.format("delta").load(delta_table_path)
# delta_df.show()

# پایان کار
spark.stop()
