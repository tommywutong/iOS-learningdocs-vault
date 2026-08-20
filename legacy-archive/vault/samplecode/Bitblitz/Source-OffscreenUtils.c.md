---
title: Bitblitz
apple_id: DTS10000066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Bitblitz/Listings/Source_OffscreenUtils_c.html
archived_at: '2026-07-18T03:01:57.267102Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Bitblitz](Bitblitz.md)


[Next](Source-OffscreenUtils.h.md)[Previous](Source-MainStuff.h.md)

# Source/OffscreenUtils.c

```c
/*--------------------------------------------------------------------------------------
//
//  File:       OffscreenUtils.c
//
//  Contents:   Procedures for the creation, manipulation, and disposal of offscreen bit structures.
//
//
//  By Georgiann ("George") Delaney
//  ©Ê1989 - 1990, Apple Computer, Inc.
//
//--------------------------------------------------------------------------------------*/


#pragma segment OffscreenSeg

#include "MacHeaders.h"


/*--------------------------------------------------------------------------------------*/
Boolean  CreateOSBitmap(GrafPtr *theOSBitmap, Rect *bounds)
/*
    CreateOSBitmap returns, in the specified pointer, an offscreen bitmap whose size is
    that which was specified in the bounds parameter.
*/
{
    GrafPtr     bitsPort;                   /*  temporary storage for new bitmap    */
    GrafPtr     holdPort;                   /*  storage for current port            */
    Rect        bitsRect;                   /*  local copy of specified boundary    */
    Boolean     theReturn    = false;       /*  temp storage for return value       */


                    /*  Save off the current port so that it can be restored after OpenPort()  */
    GetPort(&holdPort);             

                    /*  Convert the rect so that is is zero-based. */
    bitsRect = *bounds;
    OffsetRect(&bitsRect, -bitsRect.top, -bitsRect.left);

                    /*  Allocate memory for the offscreen bitmap's */
    bitsPort  = (GrafPtr) NewPtr(sizeof(GrafPort));

    if (MemError() == noErr) {
                    /*  Allocate and initialize the offscreen bitmap's clipRgn, visRgn,  etc... */
        OpenPort(bitsPort);     
        bitsPort->portRect  = bitsRect;
        RectRgn(bitsPort->clipRgn,&bitsRect);
        RectRgn(bitsPort->visRgn, &bitsRect);

                    /*  Allocate and initialize the offscreen bitmap    */
        bitsPort->portBits.bounds   = bitsRect;
        bitsPort->portBits.rowBytes = ((bitsRect.right  + 15) >> 4) << 1;
        bitsPort->portBits.baseAddr = NewPtr(bitsPort->portBits.rowBytes * (long)bitsRect.bottom);

        if (MemError() == noErr) {
                    /*  Clear the bitmap's original contents  */
            EraseRect(&bitsRect);   
            *theOSBitmap = bitsPort;
            theReturn = true;
            }
        else  {
                    /*  Offscreen bitmap alloaction failed.  Dispose all allocated memory  */
            ClosePort(bitsPort);
            DisposPtr((Ptr)bitsPort->portBits.baseAddr);
            }

                    /*  Restore the port to that which was set before OpenPort()  */
        SetPort(holdPort);  
        }

    return(theReturn);
}


/*--------------------------------------------------------------------------------------*/
void  DisposeOSBitmap(GrafPtr theOSBitmap)
/*
    DisposeOSBitmap disposes of an offscreen bitmap created with the above offscreen bitmap
    creation function.
*/
{
            /*  Close the offscreen bitmap's port  */
    ClosePort(theOSBitmap);

            /*  Dispose the offscreen bitmap  */
    DisposPtr((Ptr)theOSBitmap->portBits.baseAddr);

            /*  Dispose the offscreen bitmap's port  */
    DisposPtr((Ptr)theOSBitmap);
}
```

[Next](Source-OffscreenUtils.h.md)[Previous](Source-MainStuff.h.md)

