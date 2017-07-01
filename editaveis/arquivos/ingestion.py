def socketIngestion(args: dict) -> SparkDataFrame:
    spark = args.get("spark")
    host = args.get("host")
    port = args.get("port")
    return spark.readStream.format("socket").option("host", host) \
            .option("port", port).load()


def kafkaIngestion(args: dict) -> SparkDataFrame:
    spark = args.get("spark")
    topic = args.get("topic")
    brokers = args.get("brokers")
    return spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", brokers) \
        .option("subscribe", topic).load() \
        .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
