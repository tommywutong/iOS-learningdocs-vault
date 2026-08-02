---
title: 'CompressionSample: Compressing Blocks and Streams of Data'
apple_id: TP40016182
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CompressionSample/Listings/CompressionSample_BlockCompression_h.html
archived_at: '2026-07-18T03:04:12.128608Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CompressionSample: Compressing Blocks and Streams of Data](CompressionSample-%20Compressing%20Blocks%20and%20Streams%20of%20Data.md)


[Next](CompressionSample-StreamCompression.h.md)[Previous](CompressionSample-AAPLAppDelegate.h.md)

# CompressionSample/BlockCompression.h

```c
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides code that performs block compression.
*/

#ifndef BlockCompression_h
#define BlockCompression_h

#include "compression.h"

float doBlockCompression(FILE* fi, FILE* fo, compression_algorithm algorithm);

#endif
```

[Next](CompressionSample-StreamCompression.h.md)[Previous](CompressionSample-AAPLAppDelegate.h.md)

