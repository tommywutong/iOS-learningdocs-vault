---
title: GDevVideo
apple_id: DTS10000083
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/GDevVideo/Listings/Gen_cp.html
archived_at: '2026-07-18T03:09:42.129416Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GDevVideo](GDevVideo.md)


[Next](Document%20Revision%20History.md)[Previous](GDevVideo.md)

# Gen.cp

```c
/*
    File:       Gen.cp

    Contains:   The info includes the Base address, the rowBytes, and the depth
                of all monitors.

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
                7/9/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1
                6/10/99: (ggs) Corrected label bits per pixel

*/
#include    <ToolUtils.h>
#include    <Quickdraw.h>
#include    <StdIO.h>

main()
{
    GDHandle        theGDList;
    Ptr             theBase;
    int             theRow;
    int             theDepth;

    theGDList = GetDeviceList();

    do {
        theBase = (*(*theGDList)->gdPMap)->baseAddr;
        printf ("The GDevice I am looking at has a Base Address of %X\n", theBase);
        } while ((theGDList = GetNextDevice(theGDList)) != nil);

    theGDList = GetDeviceList();

    do {
        theRow = (*(*theGDList)->gdPMap)->rowBytes;
        theRow = theRow & 0x0000FFFF;
        printf ("The GDevice I am looking at has a Row Bytes of %X\n", theRow);
        } while ((theGDList = GetNextDevice(theGDList)) != nil);

    theGDList = GetDeviceList();

    do {
        theDepth = (*(*theGDList)->gdPMap)->pixelSize;
        theDepth = theDepth & 0x0000FFFF;
        printf ("The GDevice I am looking at has a Pixel Bit Depth of %i\n", theDepth);
        } while ((theGDList = GetNextDevice(theGDList)) != nil);

    return(0);
}
```

[Next](Document%20Revision%20History.md)[Previous](GDevVideo.md)

