---
title: GeometryTest
apple_id: DTS10000103
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/GeometryTest/Listings/GTShell_h.html
archived_at: '2026-07-18T03:10:44.400033Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GeometryTest](GeometryTest.md)


[Next](GTSupport.c.md)[Previous](GTShell.c.md)

# GTShell.h

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
    mGeometry
} ;

enum {
    iAbout = 1
} ;

enum {
    iNew = 1,
    iOpen,
    iUnused1,
    iClose,
    iSave,
    iSaveAs,
    iRevert,
    iUnused2,
    iPageSetup,
    iPrint,
    iUnused3,
    iQuit
} ;

enum { 
    iUndo,
    iUnused4,
    iCut,
    iCopy,
    iPaste,
    iClear,
    iUnused5,
    iShowClip
} ;

enum {
    iMarker = 1,
    iPoint,
    iLine, 
    iPolyline,
    iTriangle,
    iPolygon,
    iGeneralPolygon,
    iTrigrid,
    iBox,
    iMesh,
    iNurbCurve,
    iNurbPatch,
    iTorus,
    iCylinder
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

[Next](GTSupport.c.md)[Previous](GTShell.c.md)

