---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CADebugPrintf_cpp.html
archived_at: '2026-07-26T19:54:11.514032Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAHostTimeBase.cpp.md)[Previous](PublicUtility-CAStreamBasicDescription.cpp.md)

# PublicUtility/CADebugPrintf.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

//==================================================================================================
//  Includes
//==================================================================================================

//  Self Include
#include "CADebugPrintf.h"

#if DEBUG || CoreAudio_Debug

    #if TARGET_OS_WIN32
        #include <stdarg.h>
        #include <stdio.h>
        #include <Windows.h>
        extern "C"
        int CAWin32DebugPrintf(char* inFormat, ...)
        {
            char theMessage[1024];
            va_list theArguments;
            va_start(theArguments, inFormat);
            _vsnprintf(theMessage, 1024, inFormat, theArguments);
            va_end(theArguments);
            OutputDebugString(theMessage);
            return 0;
        }
    #endif

    #if defined(CoreAudio_UseSideFile)
        #include <unistd.h>
        FILE* sDebugPrintfSideFile = NULL;
        extern "C"
        void OpenDebugPrintfSideFile()
        {
            if(sDebugPrintfSideFile == NULL)
            {
                char theFileName[1024];
                snprintf(theFileName, sizeof(theFileName), CoreAudio_UseSideFile, getpid());
                sDebugPrintfSideFile = fopen(theFileName, "a+");
                DebugPrintfRtn(DebugPrintfFileComma "\n------------------------------\n");
            }
        }
    #endif

#endif
```

[Next](PublicUtility-CAHostTimeBase.cpp.md)[Previous](PublicUtility-CAStreamBasicDescription.cpp.md)

