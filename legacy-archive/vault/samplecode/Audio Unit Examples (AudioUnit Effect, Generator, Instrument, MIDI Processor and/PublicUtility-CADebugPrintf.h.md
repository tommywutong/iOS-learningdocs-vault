---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CADebugPrintf_h.html
archived_at: '2026-07-26T19:54:11.434319Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAGuard.h.md)[Previous](PublicUtility-CAAudioChannelLayout.h.md)

# PublicUtility/CADebugPrintf.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
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
        #define DebugPrintf(inFormat, ...) CAWin32DebugPrintf(informat "\n", ## __VA_ARGS__)
    #else
        #if CoreAudio_UseSysLog
            #include <sys/syslog.h>
            #define DebugPrintfRtn  syslog
            #define DebugPrintfFile LOG_NOTICE
            #define DebugPrintfLineEnding   ""
            #define DebugPrintfFileComma    DebugPrintfFile,
            #define DebugPrintf(inFormat, ...)  DebugPrintfRtn(DebugPrintfFileComma inFormat DebugPrintfLineEnding, ## __VA_ARGS__)
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
            #define DebugPrintf(inFormat, ...)  DebugPrintfRtn(DebugPrintfFileComma inFormat DebugPrintfLineEnding, ## __VA_ARGS__)
        #elif CoreAudio_UseCALog
            #include "CALog.h"
            /* We cannot use 'LOG' for 'DebugPrintfRtn' because it is a concatenating macro itself.  So we have to use syslog here. */
            #include <sys/syslog.h>
            #define DebugPrintfRtn syslog
            #define DebugPrintfFile LOG_NOTICE
            #define DebugPrintfLineEnding ""
            #define DebugPrintfFileComma DebugPrintfFile,
            /* Direct calls to 'DebugPrintf' use the new CALog system */
            #define DebugPrintf(inFormat, ...)  LOG(kLogPriority_Notice, 0, inFormat, ## __VA_ARGS__)
        #else
            #include <stdio.h>
            #define DebugPrintfRtn  fprintf
            #define DebugPrintfFile stderr
            #define DebugPrintfLineEnding   "\n"
            #define DebugPrintfFileComma    DebugPrintfFile,
            #define DebugPrintf(inFormat, ...)  DebugPrintfRtn(DebugPrintfFileComma inFormat DebugPrintfLineEnding, ## __VA_ARGS__)
        #endif
    #endif

#else
    #define DebugPrintfRtn
    #define DebugPrintfFile
    #define DebugPrintfLineEnding
    #define DebugPrintfFileComma
    #define DebugPrintf(inFormat, ...)
#endif

#endif
```

[Next](PublicUtility-CAGuard.h.md)[Previous](PublicUtility-CAAudioChannelLayout.h.md)

