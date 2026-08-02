---
title: AVAudioEngine 3D Audio Example
apple_id: TP40015163
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-11-03'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEGamingExample/Listings/AVAEGamingExample_AudioEngine_h.html
archived_at: '2026-07-18T02:59:57.242202Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVAudioEngine 3D Audio Example](AVAudioEngine%203D%20Audio%20Example.md)


[Next](LICENSE.txt.md)[Previous](AVAEGamingExample-GameViewController.h.md)

# AVAEGamingExample/AudioEngine.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    AudioEngine is the main controller class that manages the following:
                    AVAudioEngine           *_engine;
                    AVAudioEnvironmentNode  *_environment;
                    AVAudioPCMBuffer        *_collisionSoundBuffer;
                    NSMutableArray          *_collisionPlayerArray;
                    AVAudioPlayerNode       *_launchSoundPlayer;
                    AVAudioPCMBuffer        *_launchSoundBuffer;
                    bool                    _multichannelOutputEnabled;

                 It creates and connects all the nodes, loads the buffers as well as controls the AVAudioEngine object itself.
*/

@import Foundation;
@import AVFoundation;
@import SceneKit;

@protocol AudioEngineDelegate <NSObject>

@optional
- (void)engineWasInterrupted;
- (void)engineHasRestarted;
- (void)engineConfigurationHasChanged;
@end

@interface AudioEngine : NSObject

@property (weak) id<AudioEngineDelegate> delegate;
@property (nonatomic, getter=isRunning) BOOL running;

- (void)createPlayerForSCNNode:(SCNNode *)node;
- (void)destroyPlayerForSCNNode:(SCNNode *)node;

- (void)playCollisionSoundForSCNNode:(SCNNode *)node position:(AVAudio3DPoint)position impulse:(float)impulse;
- (void)playLaunchSoundAtPosition:(AVAudio3DPoint)position completionHandler:(AVAudioNodeCompletionHandler)completionHandler;

- (void)updateListenerPosition:(AVAudio3DPoint)position;
- (void)updateListenerOrientation:(AVAudio3DAngularOrientation)orientation;

-(AVAudio3DAngularOrientation)listenerAngularOrientation;
-(AVAudio3DPoint)listenerPosition;


@end
```

[Next](LICENSE.txt.md)[Previous](AVAEGamingExample-GameViewController.h.md)

