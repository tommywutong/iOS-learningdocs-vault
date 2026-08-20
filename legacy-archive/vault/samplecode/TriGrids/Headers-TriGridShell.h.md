---
title: TriGrids
apple_id: DTS10000105
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TriGrids/Listings/Headers_TriGridShell_h.html
archived_at: '2026-07-18T03:27:19.595134Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TriGrids](TriGrids.md)


[Next](Sources-GeometrySample.c.md)[Previous](Headers-TriGrid3DSupport.h.md)

# Headers/TriGridShell.h

```
// smallshell.h - public interface for the shell
//
// Modification History:
//
//  01/01/95    nick    created this file from other stuff
//  04/14/95    rdd     added menu support

#ifndef _SMALLSHELL_H_
#define _SMALLSHELL_H_

//-------------------------------------------------------------------------------------------
//
enum {
    kMenuBarRsrc = 128
} ;

enum {
    mApple = 128,
    mFile,
    mEdit,
    mGeometry,
    mTexture
} ;

enum {  // mApple
    iAbout = 1
} ;

enum {  // mFile
    iNew = 1,
    iOpen,
    iClose,
    iFileSeparator,
    iQuit
} ;

enum {  // mEdit
    iUndo = 1,
    iEditSeparator,
    iCut,
    iCopy,
    iPaste,
    iClear
} ;

enum {  // mGeometry
    iFlat = 1,
    iTorus,
    iWaveyTorus,
    iSplash,
    iSphere,
    iCone,
    iPipe,
    iSteps,
    iSpring
} ;

enum {  // mTexture
    iNoTexture = 1,
    iGeometryTexture,
    iFaceTexture,
    iTextureSeparator,
    iPictureFirst
} ;


enum {
    kWindowRsrcID = 128,
    kDialogRsrcID = 128,
    kFirstPICTRsrcID = 256
} ;

//-------------------------------------------------------------------------------------------
// globals
extern Boolean gQuitFlag ;


// function prototypes

short       HiWrd(long aLong) ;
short       LoWrd(long aLong) ;


#endif
```

[Next](Sources-GeometrySample.c.md)[Previous](Headers-TriGrid3DSupport.h.md)

