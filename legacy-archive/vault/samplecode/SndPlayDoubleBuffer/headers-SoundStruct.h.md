---
title: SndPlayDoubleBuffer
apple_id: DTS10000371
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/SndPlayDoubleBuffer/Listings/_headers_SoundStruct_h.html
archived_at: '2026-07-18T03:24:55.098617Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SndPlayDoubleBuffer](SndPlayDoubleBuffer.md)


[Next](headers-ULAW.h.md)[Previous](headers-SND.h.md)

# _headers/SoundStruct.h

```c
/*
    File:       SoundStruct.h

    Contains:   Structure that contains all the needed information for playing a sound.

    Written by: Mark Cookson    

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/31/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


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

[Next](headers-ULAW.h.md)[Previous](headers-SND.h.md)

