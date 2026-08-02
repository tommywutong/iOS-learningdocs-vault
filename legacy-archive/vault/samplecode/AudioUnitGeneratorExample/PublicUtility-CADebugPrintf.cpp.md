---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CADebugPrintf_cpp.html
archived_at: '2026-07-18T02:59:51.599671Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CADebugPrintf.h.md)[Previous](PublicUtility-CADebugMacros.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CADebugPrintf.cpp

```c
/*
 <codex> 
 <abstract>CADebugPrintf.h</abstract>
 <\codex>
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

[Next](PublicUtility-CADebugPrintf.h.md)[Previous](PublicUtility-CADebugMacros.h.md)

