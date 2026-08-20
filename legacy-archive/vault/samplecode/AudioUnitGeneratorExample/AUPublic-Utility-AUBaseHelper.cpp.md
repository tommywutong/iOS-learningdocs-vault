---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_Utility_AUBaseHelper_cpp.html
archived_at: '2026-07-18T02:59:50.146036Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-Utility-AUBaseHelper.h.md)[Previous](AUPublic-AUBase-ComponentBase.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/Utility/AUBaseHelper.cpp

```c
/*
 <codex> 
 <abstract>AUBaseHelper.h</abstract>
 <\codex>
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

// write valid samples check, with bool for zapping

UInt32 FindInvalidSamples(Float32 *inSource, UInt32 inFramesToProcess, bool &outHasNonZero, bool zapInvalidSamples)
{
    float *sourceP = inSource;

    UInt32 badSamplesDetected = 0;
    for (UInt32 i=0; i < inFramesToProcess; i++)
    {
        float  input = *sourceP;

        if(input > 0) 
            outHasNonZero = true;

        float absx = fabs(input);

        // a bad number!
        if (!(absx < 1e15))
        {
            if (!(absx == 0))
            {
                //printf("\tbad sample: %f\n", input);
                badSamplesDetected++;
                if (zapInvalidSamples)
                    *sourceP = 0;
            }
        }
        sourceP++;
    }

    return badSamplesDetected;
}


CFMutableDictionaryRef CreateFileRefDict (CFStringRef fKey, CFStringRef fPath, CFMutableDictionaryRef fileRefDict)
{
    if (!fileRefDict)
        fileRefDict = CFDictionaryCreateMutable (NULL, 0, &kCFTypeDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks);

    CFDictionarySetValue (fileRefDict, fKey, fPath);

    return fileRefDict;
}

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

[Next](AUPublic-Utility-AUBaseHelper.h.md)[Previous](AUPublic-AUBase-ComponentBase.h.md)

