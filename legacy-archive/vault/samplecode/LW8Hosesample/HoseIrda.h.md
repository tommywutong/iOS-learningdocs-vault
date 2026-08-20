---
title: LW8_Hosesample
apple_id: DTS10000295
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/LW8_Hosesample/Listings/HoseIrda_h.html
archived_at: '2026-07-18T03:13:25.822651Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LW8_Hosesample](LW8Hosesample.md)


[Next](PSWriterErr.h.md)[Previous](HoseIrda.c.md)

# HoseIrda.h

```
/*
    File:       HoseIrda.h

    Contains:   include file for Irda (Infrared) hose.

    Written by: Chorng-Shyan Lin and Ingrid Kelly   

    Copyright:  Copyright © 1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/26/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/


/*  When generating PostScript for the output stream, the converter will by default
    use, if needed, characters in the range 0x80-0xFF inclusive. Use the 'kHintEighthBitTag'
    with a value of 'false' to prevent the converter from emitting bytes with the high
    bit set.
*/
#define kHintEighthBitTag           'bit8'
#define kHintDataFormatId           1
#define kHintEighthBitId            kHintDataFormatId

/*  When generating PostScript for the output stream, the converter will by default
    use, if needed, characters in the range 0x00-0x1F inclusive. Use the 'kHintTransparentChannelTag'
    with a value of 'false' to prevent the converter from emitting bytes less than 0x20.
*/
#define kHintTransparentChannelTag  'trns'
#define kHintTransparentChannelId   1
#define kHintTransparentChannelVar  Boolean
#define kHintTransparentChannelDef  true
```

[Next](PSWriterErr.h.md)[Previous](HoseIrda.c.md)

