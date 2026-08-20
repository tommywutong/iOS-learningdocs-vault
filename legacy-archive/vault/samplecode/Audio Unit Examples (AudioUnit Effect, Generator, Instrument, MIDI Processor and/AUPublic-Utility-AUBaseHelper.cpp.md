---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_Utility_AUBaseHelper_cpp.html
archived_at: '2026-07-26T19:54:12.046406Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-Utility-AUBuffer.h.md)[Previous](AUPublic-Utility-AUMIDIDefs.h.md)

# AUPublic/Utility/AUBaseHelper.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
*/

#include "AUBaseHelper.h"

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <AudioUnit/AudioUnitProperties.h>
#else
    #include <AudioUnitProperties.h>
#endif

OSStatus    GetFileRefPath (CFDictionaryRef parent, CFStringRef frKey, CFStringRef * fPath)
{
    static CFStringRef kFRString = CFSTR (kAUPresetExternalFileRefs);

    const void* frVal = CFDictionaryGetValue(parent, kFRString);
    if (!frVal) return kAudioUnitErr_InvalidPropertyValue;

    const void* frString = CFDictionaryGetValue ((CFDictionaryRef)frVal, frKey);
    if (!frString) return kAudioUnitErr_InvalidPropertyValue;

    if (fPath)
        *fPath = (CFStringRef)frString;

    return noErr;
}

CFMutableDictionaryRef CreateFileRefDict (CFStringRef fKey, CFStringRef fPath, CFMutableDictionaryRef fileRefDict)
{
    if (!fileRefDict)
        fileRefDict = CFDictionaryCreateMutable (NULL, 0, &kCFTypeDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks);

    CFDictionarySetValue (fileRefDict, fKey, fPath);

    return fileRefDict;
}

#if TARGET_OS_MAC
// check if the URL can be accessed for reading/writing.  Returns 0 if yes, or the error value.
int AccessURLAsset(const CFURLRef inURL, int mode)
{
    char path[PATH_MAX];
    if (CFURLGetFileSystemRepresentation(inURL, TRUE, (UInt8 *)path, PATH_MAX) == FALSE)
        return kAudio_FileNotFoundError;
    // check whether we have access
    int ret = access(path, mode);
//  syslog(LOG_CRIT, "access() error is %d for \"%s\".\n", ret, path);
    if (ret == 0) return 0;
    switch (errno) {
        case EACCES:
        case EPERM:
            return -54; /*permission denied error*/
        case ENOENT:
        case ENOTDIR:
        case ELOOP:
            return kAudio_FileNotFoundError;
        default:
            return errno;
    }
}
#endif

#if DEBUG
//_____________________________________________________________________________
//
void PrintAUParamEvent (AudioUnitParameterEvent& event, FILE* f)
{
        bool isRamp = event.eventType == kParameterEvent_Ramped;
        fprintf (f, "\tParamID=%ld,Scope=%ld,Element=%ld\n", (long)event.parameter, (long)event.scope, (long)event.element);
        fprintf (f, "\tEvent Type:%s,", (isRamp ? "ramp" : "immediate"));
        if (isRamp)
            fprintf (f, "start=%ld,dur=%ld,startValue=%f,endValue=%f\n",
                    (long)event.eventValues.ramp.startBufferOffset, (long)event.eventValues.ramp.durationInFrames,
                    event.eventValues.ramp.startValue, event.eventValues.ramp.endValue);
        else
            fprintf (f, "start=%ld,value=%f\n",
                    (long)event.eventValues.immediate.bufferOffset,
                    event.eventValues.immediate.value);
        fprintf (f, "- - - - - - - - - - - - - - - -\n");
}
#endif
```

[Next](AUPublic-Utility-AUBuffer.h.md)[Previous](AUPublic-Utility-AUMIDIDefs.h.md)

