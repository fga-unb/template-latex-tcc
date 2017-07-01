def streamFilter(stream: SparkDataFrame, args: dict) -> SparkDataFrame:
    query = args.get("query")
    if (query):
        return stream.where(query)
    else:
        raise('Missing required param `query`')


def mean(stream: SparkDataFrame, args: dict) -> SparkDataFrame:
    df1 = stream.selectExpr('cast(value as double) value',
            'capability', 'uuid', 'timestamp')
    df2 = df1.select(avg("value"))
    return df2
