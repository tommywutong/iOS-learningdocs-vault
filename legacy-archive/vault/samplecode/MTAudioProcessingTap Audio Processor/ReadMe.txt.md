---
title: MTAudioProcessingTap Audio Processor
apple_id: DTS40012324
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AudioTapProcessor/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:01:31.704312Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MTAudioProcessingTap Audio Processor](MTAudioProcessingTap%20Audio%20Processor.md)


[Next](AudioTapProcessor-main.m.md)[Previous](MTAudioProcessingTap%20Audio%20Processor.md)

# ReadMe.txt

```
### AudioTapProcessor ###

===========================================================================
DESCRIPTION:

Sample application that uses the MTAudioProcessingTap in combination with AV Foundation to visualize audio samples as well as applying a Core Audio audio unit effect (Bandpass Filter) to the audio data.

Note: The sample requires at least one video asset in the Asset Library (Camera Roll) to use as the source media. It will automatically select the first one it finds.

===========================================================================
BUILD REQUIREMENTS:

Xcode 4.6.3 or later, iOS 6.1.3 or later

===========================================================================
RUNTIME REQUIREMENTS:

iOS 6.1.3 or later
iPad 2 or later iPad device

===========================================================================
PACKAGING LIST:

MYAudioTapProcessor.h & MYAudioTapProcessor.m contain the main code demonstrating the focus of this sample.

This includes setup of the AVAudioTapProcessorContext and the AVMutableAudioMix as well as instantiating the Bandpass filter Audio Unit and the render proc. which provides the demo processing being done to the audio data comming from the asset.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0 - First version WWDC 2012
Version 1.0.1 - iOS Reference Library Version

===========================================================================
Copyright (C) 2012-2013 Apple Inc. All rights reserved.
```

[Next](AudioTapProcessor-main.m.md)[Previous](MTAudioProcessingTap%20Audio%20Processor.md)

