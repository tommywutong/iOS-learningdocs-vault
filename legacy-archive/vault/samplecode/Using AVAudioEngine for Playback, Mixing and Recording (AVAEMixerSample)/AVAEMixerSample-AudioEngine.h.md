---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_AudioEngine_h.html
archived_at: '2026-07-18T02:59:58.559910Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-PlayerViewController.m.md)[Previous](AVAEMixerSample-AudioEngineViewController.m.md)

# AVAEMixerSample/AudioEngine.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    AudioEngine is the main controller class that creates the following objects:
                    AVAudioEngine               *_engine;
                    AVAudioUnitSampler          *_sampler;
                    AVAudioUnitDistortion       *_distortion;
                    AVAudioUnitReverb           *_reverb;
                    AVAudioPlayerNode           *_player;

                    AVAudioSequencer            *_sequencer;
                    AVAudioPCMBuffer            *_playerLoopBuffer;

                It connects all the nodes, loads the buffers as well as controls the AVAudioEngine object itself.
*/

@import Foundation;

// Other nodes/objects can listen to this to determine when the user finishes a recording
static NSString *kRecordingCompletedNotification = @"RecordingCompletedNotification";

static NSString *kShouldEnginePauseNotification = @"kShouldEnginePauseNotification";

@protocol AudioEngineDelegate <NSObject>
@optional
- (void)engineWasInterrupted;
- (void)engineConfigurationHasChanged;
- (void)engineHasBeenPaused;
- (void)mixerOutputFilePlayerHasStopped;
@end

@interface AudioEngine : NSObject

@property (nonatomic, readonly) BOOL recordingIsAvailable;
@property (nonatomic, readonly) BOOL playerIsPlaying;
@property (nonatomic, readonly) BOOL sequencerIsPlaying;

@property (nonatomic) float sequencerCurrentPosition;
@property (nonatomic) float sequencerPlaybackRate;

@property (nonatomic) float playerVolume;           //  0.0 - 1.0
@property (nonatomic) float playerPan;              // -1.0 - 1.0

@property (nonatomic) float samplerDirectVolume;  // 0.0 - 1.0
@property (nonatomic) float samplerEffectVolume;  // 0.0 - 1.0

@property (nonatomic) float distortionWetDryMix;    // 0.0 - 1.0
@property (nonatomic) NSInteger distortionPreset;
@property (nonatomic) float reverbWetDryMix;        // 0.0 - 1.0
@property (nonatomic) NSInteger reverbPreset;

@property (nonatomic) float outputVolume;           // 0.0 - 1.0

@property (weak) id<AudioEngineDelegate> delegate;

- (void)toggleSequencer;
- (void)togglePlayer;
- (void)toggleBuffer:(BOOL)recordBuffer;

- (void)startRecordingMixerOutput;
- (void)stopRecordingMixerOutput;

@end
```

[Next](AVAEMixerSample-PlayerViewController.m.md)[Previous](AVAEMixerSample-AudioEngineViewController.m.md)

