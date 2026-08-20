---
title: SndPlayDoubleBuffer
apple_id: DTS10000371
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/SndPlayDoubleBuffer/Listings/_headers_Private_DBFFFunctions_h.html
archived_at: '2026-07-18T03:24:54.888200Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SndPlayDoubleBuffer](SndPlayDoubleBuffer.md)


[Next](headers-ReadResource.h.md)[Previous](headers-MyGestalt.h.md)

# _headers/Private_DBFFFunctions.h

```c
/*
    File:       Private_DBFFFunctions.h

    Contains:   Headers for routines demonstrating how to deal with house keeping
                associated with playing sound.  

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

#ifndef __PRIVATE_DBFFFUNC__
#define __PRIVATE_DBFFFUNC__

#include <FSM.h>

#ifndef __INTERRUPT_ROUTINES__
#include "Interrupt_Routines.h"
#endif

#ifndef __MyAIFF__
#include "AIFF.h"
#endif

#ifndef __SND__
#include "SND.h"
#endif

#ifndef __ULAW__
#include "ULAW.h"
#endif

#ifndef __WAVE__
#include "WAVE.h"
#endif

#ifndef __LDANDFIX__
#include "LDandFix.h"
#endif

#ifndef __DEFINES__
#include "Defines.h"
#endif

/* Function declarations for private functions */
OSErr           ASoundInit              (SoundInfoPtr theSoundInfo);
Boolean         IsValid                 (SoundInfoPtr theSoundInfo);
Boolean         StrictIsValid           (SoundInfoPtr theSoundInfo);
Boolean         CheckValididity         (SoundInfoPtr theSoundInfo,
                                        Boolean strict);
pascal Boolean  ASoundFileFilter        (CInfoPBPtr theFileInfo);
OSErr           ASoundSetNumBuffers     (SoundInfoPtr theSoundInfo,
                                        long newValue);
OSErr           ASoundSetBufferSize     (SoundInfoPtr theSoundInfo,
                                        long newValue);
OSErr           ASoundSetSoundLength    (SoundInfoPtr theSoundInfo,
                                        long newValue);
OSErr           InstallCallBack         (SoundInfoPtr theSoundInfo);
OSErr           SetUpSoundHeader        (SoundInfoPtr theSoundInfo,
                                        unsigned long bufferSize);
OSErr           ASoundPrimeBuffers      (SoundInfoPtr theSoundInfo);
OSErr           PauseSound              (SoundInfoPtr theSoundInfo);
OSErr           ResumeSound             (SoundInfoPtr theSoundInfo);
Rect            GetMainScreenRect       (void);

#endif
```

[Next](headers-ReadResource.h.md)[Previous](headers-MyGestalt.h.md)

