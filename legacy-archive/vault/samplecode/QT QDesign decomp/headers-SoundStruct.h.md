---
title: QT QDesign decomp
apple_id: DTS10000911
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_QDesign_decomp/Listings/headers_SoundStruct_h.html
archived_at: '2026-07-18T03:21:23.293922Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT QDesign decomp](QT%20QDesign%20decomp.md)


[Next](source-AIFF.c.md)[Previous](headers-SetupDBHeader.h.md)

# headers/SoundStruct.h

```c
/*
**  Apple Macintosh Developer Technical Support
**
**  Structure that contains all the needed information for playing a sound.
**
**  by Mark Cookson, Apple Developer Technical Support
**
**  File:   SoundStruct.h
**
**  Copyright ©1996 Apple Computer, Inc.
**  All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "Apple Sample
**  Code" after having made changes. If you're going to re-distribute the
**  source, we require that you make it clear in the source that the code
**  was descended from Apple Sample Code, but that you've made changes.
*/

#ifndef __SOUNDSTRUCT__
#define __SOUNDSTRUCT__

#include <Files.h>
#include <Sound.h>

struct sGlobals {
    long        ggestaltSoundAttr,
                ggestaltStandardFileAttr,
                ggestaltTranslationAttr;
    Boolean     gSupports16Bit,
                gSupportsSPDB;
};

typedef struct sGlobals sGlobals;
typedef sGlobals *sGlobalsPtr;

/*
    This giant structure is in seperate file because it is trying to be
    hidden from view.  In fact there are accessor functions for most values,
    and you should use those accessors.  If you are using DBFF.h a SoundInfoPtr
    is typedef'ed to just a Ptr so that you can't see any of these fields.
*/
struct SoundInfo {
    unsigned long           signature;
    Str63                   theName;
    SndDoubleBufferHeader2  doubleHeader;
    SndChannelPtr           chan;
    SndCallBackUPP          theSoundCallBackUPP;
    sGlobals                globals;
    Fixed                   rateForResume;
    unsigned long           fileType;
    long                    numBuffers,
                            dataStart,
                            bytesTotal,
                            bytesCopied,
                            currentBuffer,
                            doubleBufferSize;
    short                   bytesPerFrame,
                            refNum,
                            vRefNum,
                            compFactor;
    Boolean                 paused,
                            playing,
                            adjusting,
                            soundDone,
                            backwards,
                            hasBeenAdjusted,
                            needsMasking,
                            stopping;
};

typedef struct SoundInfo SoundInfo;
typedef SoundInfo *SoundInfoPtr;

/*
    This is used to carry useful information to our interrupt routines.
    I wouldn't remove any fields from this structure.
*/
struct myParamBlockRec {
    ParamBlockRec           pb;
    long                    myA5;
    SndDoubleBufferPtr      theBuffer;
    SoundInfoPtr            theSoundInfo;
    Boolean                 pbInUse;
};

typedef struct myParamBlockRec myParamBlockRec;
typedef myParamBlockRec *myParmBlkPtr;

#endif
```

[Next](source-AIFF.c.md)[Previous](headers-SetupDBHeader.h.md)

