---
title: qtwiredsprites.win
apple_id: DTS10001077
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/qtwiredsprites.win/Listings/Common_Files_SpriteUtilities_h.html
archived_at: '2026-07-26T19:53:27.680744Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtwiredsprites.win](qtwiredsprites.win.md)


[Next](Common%20Files-WinFramework.c.md)[Previous](Common%20Files-SpriteUtilities.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Common Files/SpriteUtilities.h

```c
//////////
//
//  File:       SpriteUtilities.h
//
//  Contains:   Utilities for adding sprite tracks to QuickTime movies.
//
//  Written by: Sean Allen
//  Revised by: Chris Flick and Tim Monroe
//
//  Copyright:  © 1997-2000 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/10/00    rtm     cosmetic fixes to parallel changes in SpriteUtilities.c
//
//
//////////

#ifndef _SPRITEUTILITIES_
#define _SPRITEUTILITIES_

//////////
//
// header files
//
//////////

#ifndef _IMAGECOMPRESSIONUTILITIES_
#include "ImageCompressionUtilities.h"
#endif

#ifndef __ENDIANUTILITIES__
#include "EndianUtilities.h"
#endif

#ifndef __MEDIAHANDLERS__
#include <MediaHandlers.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __QUICKTIMECOMPONENTS__
#include <QuickTimeComponents.h>
#endif

#ifndef __RESOURCES__
#include <Resources.h>
#endif

//////////
//
// public utilities
//
//////////

OSErr                       SpriteUtils_SetSpriteData (QTAtomContainer theSprite, Point *theLocation, short *theVisible, short *theLayer, short *theImageIndex, ModifierTrackGraphicsModeRecord *theGraphicsMode, StringPtr theSpriteName, QTAtomContainer theActionAtoms);
OSErr                       SpriteUtils_AddSpriteToSample (QTAtomContainer theSample, QTAtomContainer theSprite, QTAtomID theSpriteID);
OSErr                       SpriteUtils_AddSpriteSampleToMedia (Media theMedia, QTAtomContainer theSample, TimeValue theDuration, Boolean isKeyFrame, TimeValue *theSampleTime);
OSErr                       SpriteUtils_AddCompressedSpriteSampleToMedia (Media theMedia, QTAtomContainer theSample, TimeValue theDuration, Boolean isKeyFrame, OSType theDataCompressorType, TimeValue *theSampleTime);
OSErr                       SpriteUtils_AddPICTImageToKeyFrameSample (QTAtomContainer theKeySample, short thePictID, RGBColor *theKeyColor, QTAtomID theID, FixedPoint *theRegistrationPoint, StringPtr theImageName);
OSErr                       SpriteUtils_AddCompressedImageToKeyFrameSample (QTAtomContainer theKeySample, ImageDescriptionHandle theImageDesc, long theDataSize, Ptr theCompressedDataPtr, QTAtomID theImageID, FixedPoint *theRegistrationPoint, StringPtr theImageName);
OSErr                       SpriteUtils_AssignImageGroupIDsToKeyFrame (QTAtomContainer theKeySample);

//////////
//
// private utilities
//
//////////

static OSErr                SpriteUtils_GetImageDescription (QTAtomContainer theKeySample, QTAtom theImagesContainerAtom, short theImageIndex, ImageDescriptionHandle theImageDesc);
static OSErr                SpriteUtils_SetImageGroupID (QTAtomContainer theKeySample, QTAtom theImagesContainerAtom, short theImageIndex, long theGroupID);
static OSErr                SpriteUtils_GetImageGroupID (QTAtomContainer theKeySample, QTAtom theImagesContainerAtom, short theImageIndex, long *theGroupID);

#endif  // _SPRITEUTILITIES_
```

[Next](Common%20Files-WinFramework.c.md)[Previous](Common%20Files-SpriteUtilities.c.md)

