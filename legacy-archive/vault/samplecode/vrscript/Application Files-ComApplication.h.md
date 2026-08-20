---
title: vrscript
apple_id: DTS10001032
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrscript/Listings/Application_Files_ComApplication_h.html
archived_at: '2026-07-26T19:53:01.569730Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrscript](vrscript.md)


[Next](Application%20Files-ComResource.h.md)[Previous](Application%20Files-ComApplication.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Application Files/ComApplication.h

```swift
//////////
//
//  File:       ComApplication.h
//
//  Contains:   Application-specific code for VRScript application.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/05/99    rtm     first file; based on earlier sample code
//
//////////

#pragma once

//////////
//
// compiler flags
//
//////////

//////////
//
// header files
//
//////////

#ifndef __MEDIAHANDLERS__
#include <MediaHandlers.h>
#endif

#ifndef __QUICKTIMEVR__
#include <QuickTimeVR.h>
#endif

#ifndef __RESOURCES__
#include <Resources.h>
#endif

#ifndef __SCRIPT__
#include <Script.h>
#endif

#ifndef __SOUND__
#include <Sound.h>
#endif

#ifndef __SOUNDSPROCKET__
#include <SoundSprocket.h>
#endif

#ifndef __TEXTUTILS__
#include <TextUtils.h>
#endif

#if TARGET_OS_MAC
#ifndef __APPLEEVENTS__
#include <AppleEvents.h>
#endif
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
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

#ifndef __URLUtilities__
#include "URLUtilities.h"
#endif

#include "ComResource.h"

#include "VRMovies.h"
#include "VR3DObjects.h"
#include "VRSound.h"
#include "VREffects.h"
#include "VRSprites.h"
#include "VRHash.h"
#include "VRPreferences.h"
#include "VRActions.h"

//////////
//
// constants
//
//////////

#define kQTMaxSoundVolume       256
#define kScriptFileSuffix       "txt"

enum {
    kScriptFileType             = FOUR_CHAR_CODE('TEXT'),
    kScriptFileCreator          = FOUR_CHAR_CODE('VRsc'),
    kPrefsFileType              = FOUR_CHAR_CODE('VRpr'),
    kPrefsFileCreator           = kScriptFileCreator
};

//////////
//
// structures
//
//////////

// application-specific data
// this data applies to a specific VR movie/window combination
typedef struct ApplicationDataRecord {

    // *** QTVR callback procedures ***
    QTVRBackBufferImagingUPP    fBackBufferProc;    // a routine descriptor for our back buffer routine
    QTVRImagingCompleteUPP      fPrescreenProc;     // a routine descriptor for our prescreen routine

    // *** General data ***
    Boolean                     fViewHasChanged;    // has the (pan, tilt, or FOV of the) view changed?
    Boolean                     fSoundHasChanged;   // has some sound changed?

    // *** Embedded QuickTime movie data ***
    Boolean                     fBackBufferIsHoriz; // is the backbuffer oriented horizontally?

    // *** SoundSprocket data ***
    SSpListenerReference        fListener;          // the single listener

    // *** 3D object data ***
    TQ3ViewObject               fView;              // the view for the scene
    GWorldPtr                   fQD3DDCGWorld;      // the offscreen graphics world used for the pixmap draw context
    Boolean                     fQD3DFOVIsVert;     // is the QD3D camera FOV vertical?
    RGBColor                    fQD3DKeyColor;      // the color for chroma key compositing for QD3D textures (this is also the background color for the QD3D draw context)

    // *** QuickTime video effects data ***
    GWorldPtr                   fSourceGWorld;      // the offscreen graphics world for the source node picture
    GWorldPtr                   fTargetGWorld;      // the offscreen graphics world for the target node picture
    ImageDescriptionHandle      fSourceGWDesc;      // the image description of the source offscreen graphics world
    ImageDescriptionHandle      fTargetGWDesc;      // the image description of the target offscreen graphics world
    VRScriptTransitionPtr       fActiveTransition;  // pointer to the list entry of the active node transition effect

    // *** Sprite data ***
    Boolean                     fMovieHasSprites;   // does the movie have a sprite track?
    MediaHandler                fSpriteHandler;     // the media handler for any sprite tracks

    // *** Wired action data ***
    Boolean                     fMovieHasActions;   // does the movie have any wired actions?

    // *** Array of our linked list head pointers ***
    struct VRScriptGeneric      *fListArray[kVRScript_FinalEntryType + 1];

} ApplicationDataRecord, *ApplicationDataPtr, **ApplicationDataHdl;

//////////
//
// function prototypes
//
//////////

#if TARGET_OS_MAC
void                    QTApp_InstallAppleEventHandlers (void);
PASCAL_RTN OSErr        QTApp_HandleOpenApplicationAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandleOpenDocumentAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandlePrintDocumentAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandleQuitApplicationAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
#endif  // TARGET_OS_MAC

// the other function prototypes are in the file MacFramework.h or WinFramework.h
```

[Next](Application%20Files-ComResource.h.md)[Previous](Application%20Files-ComApplication.c.md)

