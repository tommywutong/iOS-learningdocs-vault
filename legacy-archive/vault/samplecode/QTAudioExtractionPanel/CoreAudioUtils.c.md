---
title: QTAudioExtractionPanel
apple_id: DTS10003728
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-06-27'
source_url: https://developer.apple.com/library/archive/samplecode/QTAudioExtractionPanel/Listings/CoreAudioUtils_c.html
archived_at: '2026-07-18T03:19:57.912532Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTAudioExtractionPanel](QTAudioExtractionPanel.md)


[Next](CoreAudioUtils.h.md)[Previous](CoreAudioPlayback.h.md)

# CoreAudioUtils.c

```c
/*
 * CoreAudioUtils.c
 * Audio Extraction Panel Sample Code
 *
 * Copyright:   ©2005 by Apple Computer, Inc., all rights reserved.
 */

#include "CoreAudioUtils.h"

void ConfigureOutputDescription(ComponentDescription *inOutputDesc)
{
    inOutputDesc->componentType = kAudioUnitType_Output;
    inOutputDesc->componentSubType = kAudioUnitSubType_DefaultOutput;
    inOutputDesc->componentManufacturer = kAudioUnitManufacturer_Apple;
    inOutputDesc->componentFlags = 0;
    inOutputDesc->componentFlagsMask = 0;
}

void ConfigureScheduledPlayerDescription(ComponentDescription *inPlayerDesc)
{
    inPlayerDesc->componentType = kAudioUnitType_Generator;
    inPlayerDesc->componentSubType = kAudioUnitSubType_ScheduledSoundPlayer;
    inPlayerDesc->componentManufacturer = kAudioUnitManufacturer_Apple;
    inPlayerDesc->componentFlags = 0;
    inPlayerDesc->componentFlagsMask = 0;
}   

OSStatus SetOutputUnitStreamFormat (AudioUnit outputUnit, AudioStreamBasicDescription *asbd)
{
    return (AudioUnitSetProperty (outputUnit,
                                    kAudioUnitProperty_StreamFormat,
                                    kAudioUnitScope_Input,
                                    0,/*output*/
                                    asbd, 
                                    sizeof(AudioStreamBasicDescription)));
}

OSStatus SetPlayerUnitStreamFormat (AudioUnit playerUnit, AudioStreamBasicDescription *asbd)
{

    return   (AudioUnitSetProperty (playerUnit,
                                    kAudioUnitProperty_StreamFormat,
                                    kAudioUnitScope_Output,
                                    0,/*output*/
                                    asbd, 
                                    sizeof(AudioStreamBasicDescription)));
}

OSStatus SetOutputUnitChannelLayout(AudioUnit outputUnit, QTPropertyValuePtr layoutProperty, UInt32 size)
{
    return (AudioUnitSetProperty (outputUnit,
                                    kAudioUnitProperty_AudioChannelLayout,
                                    kAudioUnitScope_Input,
                                    0,/*output*/
                                    layoutProperty,
                                    size));
}
```

[Next](CoreAudioUtils.h.md)[Previous](CoreAudioPlayback.h.md)

