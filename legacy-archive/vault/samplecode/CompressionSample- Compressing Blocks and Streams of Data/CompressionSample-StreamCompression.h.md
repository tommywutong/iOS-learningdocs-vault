---
title: 'CompressionSample: Compressing Blocks and Streams of Data'
apple_id: TP40016182
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CompressionSample/Listings/CompressionSample_StreamCompression_h.html
archived_at: '2026-07-18T03:04:12.235373Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CompressionSample: Compressing Blocks and Streams of Data](CompressionSample-%20Compressing%20Blocks%20and%20Streams%20of%20Data.md)


[Next](CompressionSample-AAPLViewController.m.md)[Previous](CompressionSample-BlockCompression.h.md)

# CompressionSample/StreamCompression.h

```c
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides code that performs stream compression.
*/

#ifndef StreamCompression_c
#define StreamCompression_c

#include <stdio.h>
#include "compression.h"

float doStreamCompression(FILE* fi, FILE* fo, compression_algorithm algorithm, compression_stream_operation operation);

#endif
```

[Next](CompressionSample-AAPLViewController.m.md)[Previous](CompressionSample-BlockCompression.h.md)

