---
title: Speech Recognition Sample
apple_id: DTS10000374
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/Speech_Recognition_Sample/Listings/Listening_h.html
archived_at: '2026-07-18T03:25:16.683055Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Speech Recognition Sample](Speech%20Recognition%20Sample.md)


[Next](ListeningAE.c.md)[Previous](Listening.c.md)

# Listening.h

```c
/*
    File:       Listening.h

    Contains:   

    Written by:     

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/2/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#ifndef __LISTENING__
#define __LISTENING__

#include <Gestalt.h>

#ifndef __SPEAKINGERRORS__
#include "Speaking_Errors.h"
#endif

#ifndef __STRUCT__
#include "Struct.h"
#endif

OSErr       InitSpeechRecognition   (SpeechInfoPtr theSpeechInfo);
OSErr       OpenSpeechRecognition   (SpeechInfoPtr theSpeechInfo);
OSErr       ConfigureRecognition    (SpeechInfoPtr theSpeechInfo);
OSErr       GetNewRecognizer        (SpeechInfoPtr theSpeechInfo);

#endif
```

[Next](ListeningAE.c.md)[Previous](Listening.c.md)

