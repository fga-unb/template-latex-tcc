def consoleSink(stream: StructuredStream, args: dict) -> OutputStream:
    streamName = args.get("stream")
    return stream.writeStream.outputMode('append').format('console') \
            .start()


def parquetCompleteSink(stream: StructuredStream, args: dict) -> OutputStream:
    streamName = args.get("stream")
    path = args.get("path") or "/analysis"
    return stream.writeStream.outputMode('complete').format('memory') \
            .queryName('analysis').start()


def memorySink(stream: StructuredStream, args: dict) -> OutputStream:
    table = args.get('table')
    if not table:
        table = 'analysis'
    stream.writeStream.outputMode('complete').format('memory')\
            .queryName(table).start()
