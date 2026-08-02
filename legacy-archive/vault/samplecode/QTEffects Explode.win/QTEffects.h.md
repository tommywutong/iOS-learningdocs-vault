---
title: QTEffects Explode.win
apple_id: DTS10000835
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/QTEffects_Explode.win/Listings/QTEffects_h.html
archived_at: '2026-07-18T03:20:51.207096Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTEffects Explode.win](QTEffects%20Explode.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTEffects.c.md)

# QTEffects.h

```
/*
    File:       QTEffects.h

    Contains:   Code to generate a QuickTime movie with a QuickTime video effect in it.

    Written by: Scott Kuechle
                (based heavily on QuickTime SDK QTShowEffect sample code by Tim Monroe)

    Copyright:  © 1999 by Apple Computer, Inc. All rights reserved

    Change History (most recent first)

        <1>     9/25/99     srk     first file
        <2>     10/19/99    srk     changed cross fade effect to explode effect

*/

Movie                           QTEffects_CreateEffectsMovie();

static void                     QTEffects_CreateTwoTrackMovie( Movie *theMovie,
                                            short   *resRefNum,
                                            short   *resID,
                                            FSSpec  *movieFSSpec,
                                            Track   *videoTrack1,
                                            Track   *videoTrack2);
static OSErr                    QTEffects_GetPictResourceAsGWorld (short theResID,
                                                                    short theWidth,
                                                                    short theHeight,
                                                                    short theDepth,
                                                                    GWorldPtr *theGW);
static OSErr                    QTEffects_AddVideoTrackFromGWorld (Movie *theMovie,
                                                                    GWorldPtr theGW,
                                                                    Track *theSourceTrack,
                                                                    long theStartTime,
                                                                    short theWidth,
                                                                    short theHeight);
static void                     QTEffects_SetupEffectsDescription(OSType    theEffectType,
                                        ImageDescriptionHandle  *mySampleDesc,
                                        QTAtomContainer         *theEffectDesc);
static void                     QTEffects_CreateEffectsTrackAndMedia(Movie myMovie, 
                                            ImageDescriptionHandle  mySampleDesc,
                                            QTAtomContainer         theEffectDesc,
                                            Track *myTrack,
                                            Media *myMedia);
static void                     QTEffects_CreateInputMapAndAddTrackReferences(Track effectsTrack,
                                                    Media   effectsTrackMedia,
                                                    Track   sourceTrack1,
                                                    Track   sourceTrack2);                                          
static void                     QTEffects_CreateEffectDescription (OSType           theEffectName,
                                              OSType            theSourceName1,
                                              OSType            theSourceName2,
                                              QTAtomContainer   *theEffectDesc);
static void                     QTEffects_CreateEffectParameterForExplode(QTAtomContainer       myEffectDesc);
static ImageDescriptionHandle   QTEffects_MakeSampleDescription (OSType theEffectType,
                                                        short theWidth,
                                                        short theHeight);
static OSErr                    QTEffects_AddTrackReferenceToInputMap (QTAtomContainer theInputMap,
                                                                        Track theTrack,
                                                                        Track theSrcTrack,
                                                                        OSType theSrcName);
```

[Next](Document%20Revision%20History.md)[Previous](QTEffects.c.md)

