---
title: vrscript.win
apple_id: DTS10001033
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrscript.win/Listings/Feature_Files_VR3DTexture_h.html
archived_at: '2026-07-26T19:53:03.925335Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrscript.win](vrscript.win.md)


[Next](Feature%20Files-VRActions.c.md)[Previous](Feature%20Files-VR3DTexture.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Feature Files/VR3DTexture.h

```c
//////////
//
//  File:       VR3DTexture.c
//
//  Contains:   Support for adding a QuickTime movie or a picture as a texture on a QD3D object.
//
//  Written by: Tim Monroe
//              Parts modeled on BoxMoov code by Rick Evans and Robert Dierkes.
//
//  Copyright:  © 1996 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      12/16/96    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#ifndef __IMAGECOMPRESSION__
#include <ImageCompression.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __QDOFFSCREEN__
#include <QDOffscreen.h>
#endif

#ifndef __QD3D__
#include <QD3D.h>
#endif

#ifndef __QD3DGROUP__
#include <QD3DGroup.h>
#endif

#ifndef __QD3DSET__
#include <QD3DSet.h>
#endif

#ifndef __QD3DSHADER__
#include <QD3DShader.h>
#endif

#ifndef __QD3DSTORAGE__
#include <QD3DStorage.h>
#endif

#ifndef __QUICKDRAW__
#include <QuickDraw.h>
#endif

#ifndef __RESOURCES__
#include <Resources.h>
#endif

#ifndef __QTUtilities__
#include "QTUtilities.h"
#endif

#ifndef __QTVRUtilities__
#include "QTVRUtilities.h"
#endif

#ifndef __FileUtilities__
#include "FileUtilities.h"
#endif

#include "VR3DObjects.h"

//////////
//
// constants
//
//////////

#define kVR_TextureMovieVolAngle    180.0           // volume angle for all texture-mapped movies

//////////
//
// data structures
//
//////////

typedef struct {
    TQ3StoragePixmap            fStoragePixmap;     // the QD3D pixmap
    GWorldPtr                   fpGWorld;           // the offscreen buffer into which the movie or picture is drawn
    Movie                       fMovie;             // the movie source for animated textures
    MediaHandler                fMediaHandler;      // the sound media handler for animated textures
} Texture, *TexturePtr, **TextureHdl;

//////////
//
// function prototypes
//
//////////

TextureHdl                      VR3DTexture_New (char *thePathName, Boolean isTextureMovie);
TQ3Status                       VR3DTexture_AddToGroup (TextureHdl theTexture, TQ3GroupObject theGroup);
Boolean                         VR3DTexture_Delete (TextureHdl theTexture);
Boolean                         VR3DTexture_NextFrame (TextureHdl theTexture);
```

[Next](Feature%20Files-VRActions.c.md)[Previous](Feature%20Files-VR3DTexture.c.md)

