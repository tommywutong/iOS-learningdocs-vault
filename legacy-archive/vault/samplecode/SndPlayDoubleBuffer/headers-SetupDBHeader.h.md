---
title: SndPlayDoubleBuffer
apple_id: DTS10000371
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/SndPlayDoubleBuffer/Listings/_headers_SetupDBHeader_h.html
archived_at: '2026-07-18T03:24:55.030215Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SndPlayDoubleBuffer](SndPlayDoubleBuffer.md)


[Next](headers-SimpleAppSound.h.md)[Previous](headers-ReadResource.h.md)

# _headers/SetupDBHeader.h

```c
/*
    File:       SetupDBHeader.h

    Contains:   Headers for routine demonstrating how to set up a DoubleBufferHeader sound header.

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
#ifndef __SETUPDBHEADER__
#define __SETUPDBHEADER__

#include <AIFF.h>
#include <Sound.h>
#include <SoundComponents.h>

#ifndef __SOUNDSTRUCT__
#include "SoundStruct.h"
#endif

#ifndef __DEFINES__
#include "Defines.h"
#endif

OSErr   SetupDBHeader   (SoundInfoPtr theSoundInfo,
                        Fixed sampleRate,
                        short sampleSize,
                        short numChannels,
                        short compressionID,
                        long compressionType);

#endif
```

[Next](headers-SimpleAppSound.h.md)[Previous](headers-ReadResource.h.md)

