---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CADebugPrintf_h.html
archived_at: '2026-07-18T02:59:51.643065Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CAException.h.md)[Previous](PublicUtility-CADebugPrintf.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CADebugPrintf.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
*/
#if !defined(__CADebugPrintf_h__)
#define __CADebugPrintf_h__

//=============================================================================
//  Includes
//=============================================================================

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreAudio/CoreAudioTypes.h>
#else
    #include "CoreAudioTypes.h"
#endif

//=============================================================================
//  Macros to redirect debugging output to various logging services
//=============================================================================

//#define   CoreAudio_UseSysLog     1
//#define   CoreAudio_UseSideFile   "/CoreAudio-%d.txt"

#if DEBUG || CoreAudio_Debug

    #if TARGET_OS_WIN32
        #if defined(__cplusplus)
        extern "C"
        #endif
        extern int CAWin32DebugPrintf(char* inFormat, ...);
        #define DebugPrintfRtn          CAWin32DebugPrintf
        #define DebugPrintfFile         
        #define DebugPrintfLineEnding   "\n"
        #define DebugPrintfFileComma
    #else
        #if CoreAudio_UseSysLog
            #include <sys/syslog.h>
            #define DebugPrintfRtn  syslog
            #define DebugPrintfFile LOG_NOTICE
            #define DebugPrintfLineEnding   ""
            #define DebugPrintfFileComma    DebugPrintfFile,
        #elif defined(CoreAudio_UseSideFile)
            #include <stdio.h>
            #if defined(__cplusplus)
            extern "C"
            #endif
            void OpenDebugPrintfSideFile();
            extern FILE* sDebugPrintfSideFile;
            #define DebugPrintfRtn  fprintf
            #define DebugPrintfFile ((sDebugPrintfSideFile != NULL) ? sDebugPrintfSideFile : stderr)
            #define DebugPrintfLineEnding   "\n"
            #define DebugPrintfFileComma    DebugPrintfFile,
        #else
            #include <stdio.h>
            #define DebugPrintfRtn  fprintf
            #define DebugPrintfFile stderr
            #define DebugPrintfLineEnding   "\n"
            #define DebugPrintfFileComma    DebugPrintfFile,
        #endif
    #endif

    #define DebugPrintf(inFormat, ...)  DebugPrintfRtn(DebugPrintfFileComma inFormat DebugPrintfLineEnding, ## __VA_ARGS__)
#else
    #define DebugPrintfRtn  
    #define DebugPrintfFile 
    #define DebugPrintfLineEnding   
    #define DebugPrintfFileComma
    #define DebugPrintf(inFormat, ...)
#endif


#endif
```

[Next](PublicUtility-CAException.h.md)[Previous](PublicUtility-CADebugPrintf.cpp.md)

