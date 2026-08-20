---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_AudioController_h.html
archived_at: '2026-07-18T03:28:52.240077Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](Classes-BufferManager.cpp.md)[Previous](Classes-EAGLView.mm.md)

# Classes/AudioController.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class demonstrates the audio APIs used to capture audio data from the microphone and play it out to the speaker. It also demonstrates how to play system sounds

 */

#import <AudioToolbox/AudioToolbox.h>
#import <AVFoundation/AVFoundation.h>

#import "BufferManager.h"
#import "DCRejectionFilter.h"


@interface AudioController : NSObject {

    AudioUnit               _rioUnit;
    BufferManager*          _bufferManager;
    DCRejectionFilter*      _dcRejectionFilter;
    AVAudioPlayer*          _audioPlayer;   // for button pressed sound
    BOOL                    _audioChainIsBeingReconstructed;
}

@property (nonatomic, assign) BOOL muteAudio;
@property (nonatomic, assign, readonly) BOOL audioChainIsBeingReconstructed;

- (BufferManager*) getBufferManagerInstance;
- (OSStatus)    startIOUnit;
- (OSStatus)    stopIOUnit;
- (void)        playButtonPressedSound;
- (double)      sessionSampleRate;

@end
```

[Next](Classes-BufferManager.cpp.md)[Previous](Classes-EAGLView.mm.md)

