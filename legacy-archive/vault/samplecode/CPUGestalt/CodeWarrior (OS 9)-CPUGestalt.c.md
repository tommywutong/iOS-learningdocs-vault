---
title: CPUGestalt
apple_id: DTS10000725
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/CPUGestalt/Listings/CodeWarrior____OS_9__CPUGestalt_c.html
archived_at: '2026-07-18T03:02:42.839902Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CPUGestalt](CPUGestalt.md)


[Next](ProjectBuilder%20%28OS%20X%29-CPUGestalt.c.md)[Previous](CPUGestalt.md)

# CodeWarrior (OS 9)/CPUGestalt.c

```c
/*
    File:       CPUGestalt.c

    Contains:   This sample code illustrates the way to determine the 
                processor type of the Macintosh you're running on   


    Written by:     

    Copyright:  Copyright © 1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/23/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1 and
                                            Added PowerPC 750 processor


*/

#include <Gestalt.h>
#include <stdio.h>

void main()
{
    OSErr   err;
    long    getCPUtype;

    // check to see if we're on a Power Macintosh
    err = Gestalt (gestaltNativeCPUtype, &getCPUtype);

    if (0x100 & getCPUtype) {
        // we are on a Power Macintosh
        if (getCPUtype == gestaltCPU601)
            printf( "\nThis is a Power Macintosh with a 601 processor." );
        else if (getCPUtype == gestaltCPU603)
            printf( "\nThis is a Power Macintosh with a 603 processor." );
        else if (getCPUtype == gestaltCPU604)
            printf( "\nThis is a Power Macintosh with a 604 processor." );
        else if (getCPUtype==gestaltCPU750)
            printf( "\nThis is a Power Macintosh with a 750(G3) processor." );
        else
            printf( "\nThis is a Power Macintosh with a processor that I am unaware of." );
    } else {
        // we are on a 68K Macintosh
        err = Gestalt ( gestaltProcessorType, &getCPUtype );
        if (getCPUtype == gestalt68040)
            printf( "\nThis is a 68K Macintosh with a 68040 processor." );
        else if (getCPUtype == gestalt68030)
            printf( "\nThis is a 68K Macintosh with a 68030 processor." );
        else if (getCPUtype == gestalt68020)
            printf( "\nThis is a 68K Macintosh with a 68020 processor." );
        else if (getCPUtype == gestalt68010)
            printf( "\nThis is a 68K Macintosh with a 68010 processor." );
        else if (getCPUtype == gestalt68000)
            printf( "\nThis is a 68K Macintosh with a 68000 processor." );
        else
            printf( "\nThis is a 68K Macintosh with a processor that I am unaware of." );
    }
}
```

[Next](ProjectBuilder%20%28OS%20X%29-CPUGestalt.c.md)[Previous](CPUGestalt.md)

