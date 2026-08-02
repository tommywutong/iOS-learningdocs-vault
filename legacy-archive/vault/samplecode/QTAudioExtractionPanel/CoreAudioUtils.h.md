---
title: QTAudioExtractionPanel
apple_id: DTS10003728
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-06-27'
source_url: https://developer.apple.com/library/archive/samplecode/QTAudioExtractionPanel/Listings/CoreAudioUtils_h.html
archived_at: '2026-07-18T03:19:57.964885Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTAudioExtractionPanel](QTAudioExtractionPanel.md)


[Next](InfoForCallback.h.md)[Previous](CoreAudioUtils.c.md)

# CoreAudioUtils.h

```c
/*
 * CoreAudioUtils.h
 * Audio Extraction Panel Sample Code
 *
 * Copyright:   ©2005 by Apple Computer, Inc., all rights reserved.
 */

#include <Carbon/Carbon.h>
#include <QuickTime/QuickTime.h>
#include <AudioUnit/AudioUnit.h>
#include <AudioToolbox/AudioToolbox.h>

extern void ConfigureOutputDescription(ComponentDescription *inOutputDesc);
extern void ConfigureScheduledPlayerDescription(ComponentDescription *inPlayerDesc);
extern OSStatus SetOutputUnitStreamFormat (AudioUnit outputUnit, AudioStreamBasicDescription *asbd);
extern OSStatus SetPlayerUnitStreamFormat (AudioUnit playerUnit, AudioStreamBasicDescription *asbd);
extern OSStatus SetOutputUnitChannelLayout (AudioUnit outputUnit, QTPropertyValuePtr layoutProperty, UInt32 size);
```

[Next](InfoForCallback.h.md)[Previous](CoreAudioUtils.c.md)

