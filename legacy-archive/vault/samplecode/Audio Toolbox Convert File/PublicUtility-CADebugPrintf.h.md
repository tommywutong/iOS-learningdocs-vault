---
title: Audio Toolbox Convert File
apple_id: DTS40008649
resource_type: Sample Code
platform: watchOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-09-29'
source_url: https://developer.apple.com/library/archive/samplecode/ConvertFile/Listings/PublicUtility_CADebugPrintf_h.html
archived_at: '2026-07-18T03:04:16.684724Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Toolbox Convert File](Audio%20Toolbox%20Convert%20File.md)


[Next](PublicUtility-CAXException.h.md)[Previous](PublicUtility-CAXException.cpp.md)

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

[Next](PublicUtility-CAXException.h.md)[Previous](PublicUtility-CAXException.cpp.md)

