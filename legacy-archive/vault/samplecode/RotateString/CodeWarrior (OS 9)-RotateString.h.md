---
title: RotateString
apple_id: DTS10000161
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/RotateString/Listings/CodeWarrior____OS_9__RotateString_h.html
archived_at: '2026-07-18T03:22:22.439240Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RotateString](RotateString.md)


[Next](ProjectBuilder%20%28OS%20X%29-CarbonPrefix.h.md)[Previous](CodeWarrior%20%28OS%209%29-RotateString.c.md)

# CodeWarrior (OS 9)/RotateString.h

```c
/*
    File:       RotateString.h

    Contains:   

    Written by: Randy Theland and Brigham Stevens   

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/14/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#include <Types.h>
#include <Quickdraw.h>

typedef enum { clockWise, counterClockWise } rotDir;

pascal OSErr RotateString( Str255 str, BitMap *destMap, short direction);
```

[Next](ProjectBuilder%20%28OS%20X%29-CarbonPrefix.h.md)[Previous](CodeWarrior%20%28OS%209%29-RotateString.c.md)

