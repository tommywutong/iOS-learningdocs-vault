---
title: Bitblitz
apple_id: DTS10000066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Bitblitz/Listings/LibHeaders_ColorTools_h.html
archived_at: '2026-07-18T03:01:55.309265Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Bitblitz](Bitblitz.md)


[Next](LibHeaders-MacHeaders.h.md)[Previous](LibHeaders-AutoCursor.h.md)

# LibHeaders/ColorTools.h

```swift
#ifndef __COLORTOOLS__
#define __COLORTOOLS__

/*---------------------------------------------------------------------------------------
//  File:   ColorTools.h    
//  Date:   February 15, 1989   
//
//  by Mike Puckett, Macintosh CPU Software Quality, x4-1332.
//  ©Ê1989 - 1990, Apple Computer, Inc.
//---------------------------------------------------------------------------------------
*/

/* Useful Definitions -------------------------------------------------------------------
*/
#define hilite      (short)50               /* This should be defined in QuickDraw.h!   */
#define dither      (short)64               /* Only if Jackson Pollock is around.       */

#define FULL_HUE    (unsigned short)0xFFFF
#define NO_HUE      (unsigned short)0x0000 


/* Useful Macros ------------------------------------------------------------------------
*/
#define ISCGRAFPORT(grafPtr)    (TEST_FLAG(((GrafPtr)grafPtr)->portBits.rowBytes,0xC000))
#define PM_ROWBYTES(rb)         ((unsigned short)0x8000 | (rb))


/* Useful In-Lines ----------------------------------------------------------------------
*/
pascal unsigned long
QDVersion(void) = 
{   0x7014, /* Moveq    #$14,D0 */
    0xAB1D  /* _Offscreen       */
    };

/* Data Structures ----------------------------------------------------------------------
*/
typedef struct
{   RGBColor    mTtlColor,
                mBkGColor,
                mBarColor,
                mItmColor,
                mItmMark,
                mItmCmnd;
    }
MColorsType;


#ifdef __safe_link
extern "C" {
#endif

extern pascal   void    InitColorTools(                     void);

/* General Purpose Routines -------------------------------------------------------------
*/
extern pascal   Boolean HasColorQD(                         void);

extern pascal   Boolean Has32BitQD(                         void);

extern pascal   void    HiliteRect(         Rect            *theRect);

extern pascal   void    HiliteRoundRect(    Rect            *theRect,
                                            short           ovalWidth,
                                            short           ovalHeight);

extern pascal   void    HiliteRgn(          RgnHandle       theRgn);

extern pascal   Boolean PlotIcls(           Rect            *theRect,
                                            ResType         iclsType,
                                            short           iclsID);

extern pascal   void    PixToBits(          PixMapHandle    pmHandle,
                                            BitMap          *bitMap);


extern pascal   void    GetColorEntry(      CTabHandle      theCTable,
                                            short           theType,
                                            RGBColor        *colorEntry);

/* Window-Oriented Routines -------------------------------------------------------------
*/
extern pascal void      GetWColor(          WindowPtr       theWindow,
                                            short           theType,
                                            RGBColor        *theColor);

/* Control-Oriented Routines ------------------------------------------------------------
*/
extern pascal void      GetCtlColor(        ControlHandle   theControl,
                                            short           theType,
                                            RGBColor        *theColor);

/* Menu-Oriented Routines ---------------------------------------------------------------
*/
extern pascal void      SetMenuItemColor(   short           menuID,
                                            short           menuItem,
                                            RGBColor        *itemColor);

extern pascal void      GetMColors(         short           menuID,
                                            short           menuItem,
                                            MColorsType     *mColors);


#ifdef __safe_link
}
#endif


#endif
```

[Next](LibHeaders-MacHeaders.h.md)[Previous](LibHeaders-AutoCursor.h.md)

