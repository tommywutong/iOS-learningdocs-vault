---
title: Bitblitz
apple_id: DTS10000066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Bitblitz/Listings/LibHeaders_WCenter_h.html
archived_at: '2026-07-18T03:01:55.602687Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Bitblitz](Bitblitz.md)


[Next](Resources-AlertDlogUtils.r.md)[Previous](LibHeaders-PictUtils.h.md)

# LibHeaders/WCenter.h

```
#ifndef __WCENTER__
#define __WCENTER__

/*---------------------------------------------------------------------------------------
//  File:       WCenter.h   
//  Date:       February 13, 1989
//
//  by Mike Puckett, Macintosh CPU Software Quality, x4-1332.
//  © 1989 - 1990, Apple Computer, Inc.
//---------------------------------------------------------------------------------------
*/

/* Useful constants ---------------------------------------------------------------------
*/

#ifdef THINK_C
#undef  topLeft
#undef  botRight

#define zoomDocProc  8
#define zoomNoGrow  12
#endif

#define doMFAdjust  true            /* For use with GetCurScreenRect()  */
#define ignoreMF    false

enum
{   bothHV = 1,
    hOnly,
    vOnly,
    vThird
    };
typedef short CenteringType;

enum                                /* tic-tac-toe:         */
{   topLeft = 1,                    /* ------------         */
    botLeft,                        /*      tL  mT  tR      */
    topRight,                       /*      mL  XX  mR      */                              
    botRight,                       /*      bL  mB  bR      */
    midTop,
    midLeft,
    midBot,
    midRight
    };
typedef short CorneringType;

enum
{   resizeInPlace,                  /* resize from t,l      */  
    resizeFromZero,                 /* resize from 0,0      */
    resizeV2Scrn,                   /* resize to Screen V,h */
    resizeH2Scrn,                   /* resize to Screen H,v */          
    resizeBothHV2Scrn               /* resize to Screen H,V */
    };
typedef short ResizingType;


#ifndef THINK_C
    typedef pascal GDHandle (* CenteringProcPtr)(ResType resType, short resID, short constraint);
#else
    typedef ProcPtr CenteringProcPtr;
#endif

#ifdef __safe_link
extern "C" {
#endif

extern pascal void      InitWCenter(                        void);

/* The routines -------------------------------------------------------------------------
//
// GetRectGDevice() is a utility routine used by GetCurScreenRect(),
// and should not be used unless GDevices exists.  The routines
// that use GetCurScreenRect(), like SetZoom2CurScreen(), return
// nil on machines where GDevices donÕt exists.
*/
extern pascal short     HRectLength(        Rect            *theRect);

extern pascal short     VRectLength(        Rect            *theRect);

extern pascal void      CenterOfRect(       Rect            *theRect,
                                            Point           *thePoint);

extern pascal GDHandle  GetRectGDevice(     Rect            *srcRect);

extern pascal GDHandle  GetCurScreenRect(   Rect            *srcRect,
                                            Rect            *screenRect,
                                            Boolean         mfAdjust);

extern pascal void      GetCurSrcRect(      Rect            *srcRect);

extern        short     DeltaTop(           ResType         resID,
                                            short           wVariant);
extern        short     DeltaLeft(          ResType         resID,
                                            short           wVariant);

extern pascal GDHandle  SetZoom2CurScreen(  WindowPtr       theWindow);


extern pascal void      CenterWRectToXRect( ResType         resType,
                                            short           resID,
                                            Rect            *theXRect,
                                            CenteringType   constraint);

extern pascal void      CornerWRectToXRect( ResType         resType,
                                            short           resID,
                                            Rect            *theXRect,
                                            CorneringType   constraint);

extern pascal GDHandle  CenterWRsrc(        ResType         resType,
                                            short           resID,
                                            CenteringType   constraint);

extern pascal GDHandle  CornerWRsrc(        ResType         resType,
                                            short           resID,
                                            CorneringType   constraint);

extern pascal void      ResizeWRsrc(        ResType         resType,
                                            short           resID,
                                            Point           size,
                                            ResizingType    constraint);

extern pascal GDHandle  OffsetWRsrc(        ResType         resType,
                                            short           resID,  
                                            short           wCount);

extern pascal void      GetDLOGTemplate(    short           resID,
                                            DialogTPtr      dlogTPtr);
extern pascal void      SetDLOGTemplate(    short           resID,
                                            DialogTPtr      dlogTPtr);

#ifdef __safe_link
}
#endif

#endif
```

[Next](Resources-AlertDlogUtils.r.md)[Previous](LibHeaders-PictUtils.h.md)

