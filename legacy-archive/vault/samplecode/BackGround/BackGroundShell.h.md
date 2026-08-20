---
title: BackGround
apple_id: DTS10000107
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BackGround/Listings/BackGroundShell_h.html
archived_at: '2026-07-18T03:01:41.998474Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BackGround](BackGround.md)


[Next](BackGroundSupport.c.md)[Previous](BackGroundShell.c.md)

# BackGroundShell.h

```
// Quickdraw 3D sample code
//
// Nick Thompson, AppleLink: DEVSUPPORT (devsupport@applelink.apple.com)
//
// ©1994-5 Apple Computer Inc., All Rights Reserved

#ifndef _SMALLSHELL_H_
#define _SMALLSHELL_H_


//-------------------------------------------------------------------------------------------
//
enum {
    mApple = 128,
    mFile,
    mEdit,
    mTest
} ;

enum {
    iAbout = 1
} ;

enum {
    iNew = 1,
    iOpen,
    iClose,
    iUnused1,
    iQuit
} ;

//-------------------------------------------------------------------------------------------
//
enum {
    iUsePictPalette = 1
} ;

//-------------------------------------------------------------------------------------------
// globals - defined in SmallShell.c
extern Boolean gQuitFlag ;


//-------------------------------------------------------------------------------------------
// constants - defined in SmallShell.c
extern const RGBColor   kRGBBlack ;
extern const RGBColor   kRGBWhite ;

// function prototypes


WindowPtr   DoCreateBufferedWindow( Rect *theRect, 
                                    const Ptr theStorage, 
                                    const CTabHandle theWindowCTab,
                                    const short theDepth, 
                                    const Str255 theTitle ) ;
short       HiWrd(long aLong) ;
short       LoWrd(long aLong) ;


#endif
```

[Next](BackGroundSupport.c.md)[Previous](BackGroundShell.c.md)

