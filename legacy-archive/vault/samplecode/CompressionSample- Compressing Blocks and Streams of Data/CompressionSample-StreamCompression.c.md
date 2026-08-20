---
title: 'CompressionSample: Compressing Blocks and Streams of Data'
apple_id: TP40016182
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CompressionSample/Listings/CompressionSample_StreamCompression_c.html
archived_at: '2026-07-18T03:04:12.172430Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CompressionSample: Compressing Blocks and Streams of Data](CompressionSample-%20Compressing%20Blocks%20and%20Streams%20of%20Data.md)


[Next](CompressionSample-AAPLAppDelegate.m.md)[Previous](CompressionSample-main.m.md)

# CompressionSample/StreamCompression.c

```c
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides code that performs stream compression.
*/

#include "StreamCompression.h"
#include <stdlib.h>

// These buffer sizes are arbitrary. Choose sizes to suit your own purposes.
#define inBufSize 256
#define outBufSize 1024

float doStreamCompression(FILE* fi, FILE* fo, compression_algorithm algorithm, compression_stream_operation operation)
{
    uint8_t *dstBuf = malloc(outBufSize);
    uint8_t *srcBuf = malloc(inBufSize);
    compression_status status;
    size_t size_read;
    size_t size_written;
    float totalInputSize = 0;
    float totalOutputSize = 0;
    compression_stream_flags flags;
    compression_stream stream;

    compression_stream_init(&stream, operation, algorithm);
    stream.dst_ptr = dstBuf;
    stream.dst_size = outBufSize;
    stream.src_ptr = srcBuf;
    stream.src_size = 0;
    flags = 0;

    do {
        if (stream.src_size == 0) {
            // Input buffer empty.
            if (flags != COMPRESSION_STREAM_FINALIZE || operation == COMPRESSION_STREAM_ENCODE) {
                // Refill srcBuf.
                size_read = fread(srcBuf, 1, inBufSize, fi);
                totalInputSize += size_read;
                stream.src_ptr = srcBuf;
                stream.src_size = size_read;

                if (size_read < inBufSize) {
                    // Reached end of data.
                    flags = COMPRESSION_STREAM_FINALIZE;
                }
            }
        }
        if (stream.dst_size == 0) {
            // Output buffer full.

            // Write out dstbuf.
            size_written = fwrite(dstBuf, 1, outBufSize, fo);
            totalOutputSize += size_written;

            // Re-use dstBuf.
            stream.dst_ptr = dstBuf;
            stream.dst_size = outBufSize;
        }

        // Compress.
        status = compression_stream_process(&stream, flags);
        switch (status) {
            case COMPRESSION_STATUS_OK:
                // We are going to call compression_stream_process at least once more, so we prepare for that.
                if (stream.dst_size == 0) {
                    // Output buffer full.

                    // Write out dstbuf.
                    size_written = fwrite(dstBuf, 1, outBufSize, fo);
                    totalOutputSize += size_written;

                    // Re-use dstBuf.
                    stream.dst_ptr = dstBuf;
                    stream.dst_size = outBufSize;
                }

                break;

            case COMPRESSION_STATUS_END:
                // We are done, just write out the output buffer if there's anything in it.
                if (stream.dst_ptr > dstBuf) {
                    // Write out dstbuf.
                    size_written = fwrite(dstBuf, 1, stream.dst_ptr - dstBuf, fo);
                    totalOutputSize += size_written;
                }

                break;

            case COMPRESSION_STATUS_ERROR:
                return 0;

            default:
                break;
        }
    } while (status == COMPRESSION_STATUS_OK);

    compression_stream_destroy(&stream);

    return totalInputSize / totalOutputSize;
}
```

[Next](CompressionSample-AAPLAppDelegate.m.md)[Previous](CompressionSample-main.m.md)

