---
title: SndPlayDoubleBuffer
apple_id: DTS10000371
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/SndPlayDoubleBuffer/Listings/_headers_MungeBuffer_h.html
archived_at: '2026-07-18T03:24:54.778910Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SndPlayDoubleBuffer](SndPlayDoubleBuffer.md)


[Next](headers-MyAIFF.h.md)[Previous](headers-LDandFix.h.md)

# _headers/MungeBuffer.h

```c
/*
    File:       MungeBuffer.h

    Contains:   Headers for routines demonstrating how to manipulate buffers containing WAVE sounds.

    Written by: Mark Cookson    

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/31/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#ifndef __MUNGEBUFFER__
#define __MUNGEBUFFER__

#include <Types.h>

#ifndef __DEFINES__
#include "Defines.h"
#endif

/* Comment out the next line to use C functions instead of assembly functions. */
#define ASM

#ifdef ASM

asm void    Endian16BitBuffer           (Ptr buf,
                                        unsigned long count);
#else

    void    Endian16BitBuffer           (Ptr buf,
                                        unsigned long count);

#endif

void ReverseMono8BitBuffer (const Ptr buf, unsigned long count);
void ReverseStereo8BitBuffer (const Ptr buf, unsigned long count);
void ReverseMono16BitBuffer (const Ptr buf, unsigned long count);
void ReverseStereo16BitBuffer (const Ptr buf, unsigned long count);

#endif
```

[Next](headers-MyAIFF.h.md)[Previous](headers-LDandFix.h.md)

