---
title: BoxTex
apple_id: DTS10000101
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxTex/Listings/BoxTexShell_h.html
archived_at: '2026-07-18T03:02:15.937543Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxTex](BoxTex.md)


[Next](Textures.c.md)[Previous](BoxTexShell.c.md)

# BoxTexShell.h

```
// smallshell.h - public interface for the shell
//
// Modification History:
//
//  01/01/95    nick    created this file from other stuff

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

[Next](Textures.c.md)[Previous](BoxTexShell.c.md)

