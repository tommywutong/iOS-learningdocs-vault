---
title: SndPlayDoubleBuffer
apple_id: DTS10000371
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/SndPlayDoubleBuffer/Listings/_headers_SND_h.html
archived_at: '2026-07-18T03:24:54.988888Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SndPlayDoubleBuffer](SndPlayDoubleBuffer.md)


[Next](headers-SoundStruct.h.md)[Previous](headers-SimpleAppSound.h.md)

# _headers/SND.h

```c
/*
    File:       SND.h

    Contains:   Header file for routines demonstrating how to parse 'snd ' resource files.

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

#ifndef __SND__
#define __SND__

#include <Resources.h>
#include <Sound.h>
#include <SoundComponents.h>
#include <SoundInput.h>

#ifndef __SETUPDBHEADER__
#include "SetupDBHeader.h"
#endif

#ifndef __READRESOURCE__
#include "ReadResource.h"
#endif

#ifndef __DEFINES__
#include "Defines.h"
#endif

typedef union {
    SoundHeaderPtr          standardHeaderPtr;
    ExtSoundHeaderPtr       extendedHeaderPtr;
    CmpSoundHeaderPtr       compressedHeaderPtr;
}headerTemplate, *headerTemplatePtr;

        OSErr   ASoundGetSNDHeader      (SoundInfoPtr theSoundInfo,
                                        long *dataStart,
                                        long *length);

        OSErr   MyParseSndHeader        (SndListHandle theSoundHeader,
                                        SoundComponentData *sndInfo,
                                        unsigned long *numFrames,
                                        unsigned long *dataOffset);

#endif
```

[Next](headers-SoundStruct.h.md)[Previous](headers-SimpleAppSound.h.md)

