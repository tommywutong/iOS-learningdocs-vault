---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/Source_echoTouchHelper_h.html
archived_at: '2026-07-18T03:29:08.826915Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](Source-echoTouchAppDelegate.h.md)[Previous](Source-ViewController.h.md)

# Source/echoTouchHelper.h

```c
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Basic Utility Functions
*/

#include <AudioToolbox/AudioToolbox.h>

void LoadVoiceFileDataToMemory(CFURLRef inURL,
                               AudioStreamBasicDescription &outFileDesc,
                               UInt64 &outFileSize,
                               void* &outFileData);

OSStatus SetupOutputUnit(AURenderCallbackStruct inInputProc,
                         AURenderCallbackStruct inRenderProc,
                         AudioUnit &outUnit,
                         const AudioStreamBasicDescription &voiceFormat);
```

[Next](Source-echoTouchAppDelegate.h.md)[Previous](Source-ViewController.h.md)

