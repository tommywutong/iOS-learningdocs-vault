---
title: Speech Recognition Sample
apple_id: DTS10000374
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/Speech_Recognition_Sample/Listings/SpeechCallbacks_c.html
archived_at: '2026-07-18T03:25:16.926566Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Speech Recognition Sample](Speech%20Recognition%20Sample.md)


[Next](SpeechCallbacks.h.md)[Previous](SpeakingErrors.h.md)

# SpeechCallbacks.c

```c
/*
    File:       SpeechCallbacks.c

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
#ifndef __SPEACHCALLBACKS__
#include "SpeechCallbacks.h"
#endif

OSErr       SetSpeechDoneCallback   (const SpeechChannel theSpeechChan)
{
    OSErr       theErr      = noErr;

    theErr = SetSpeechInfo (theSpeechChan, soSpeechDoneCallBack, NewSpeechDoneProc (SpeechDoneCallback));
    if (theErr != noErr) {
        DebugStr ("\pSetSpeechInfo (SetSpeechDoneCallback) error");
    }

    return theErr;
}

OSErr       SetWordCallback         (const SpeechChannel theSpeechChan)
{
    OSErr       theErr      = noErr;

    theErr = SetSpeechInfo (theSpeechChan, soWordCallBack, NewSpeechWordProc (WordCallback));
    if (theErr != noErr) {
        DebugStr ("\pSetSpeechInfo (SetWordCallback) error");
    }

    return theErr;
}

pascal void SpeechDoneCallback      (const SpeechChannel theSpeechChan,
                                    const long refCon)
{
#pragma unused (theSpeechChan)

    if (refCon == 'test') {
//      DebugStr ("\pEntering MySpeechDoneCallback, all is good.");
    }
    else {
        DebugStr ("\pEntering MySpeechDoneCallback, all is NOT good.");
    }   
}

pascal void WordCallback            (const SpeechChannel theSpeechChan,
                                    const long refCon,
                                    const long wordPos,
                                    const short wordLen)
{
#pragma unused (theSpeechChan)
#pragma unused (wordPos)
#pragma unused (wordLen)

    if (refCon == 'test') {
//      DebugStr ("\pEntering MyWordCallback, all is good.");
    }
    else {
        DebugStr ("\pEntering MyWordCallback, all is NOT good.");
    }   
}
```

[Next](SpeechCallbacks.h.md)[Previous](SpeakingErrors.h.md)

