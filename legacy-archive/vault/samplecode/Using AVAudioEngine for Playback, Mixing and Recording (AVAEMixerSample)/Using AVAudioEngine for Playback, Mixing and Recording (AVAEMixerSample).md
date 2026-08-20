---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Introduction/Intro.html
archived_at: '2026-07-18T02:59:58.322808Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AVAEMixerSample-main.m.md)

# Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.3, 2017-03-23 handleMediaServicesReset now configures AVAudioSession per QA1749 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcmzufvjgk5tjonuw63sinfzxi33spewui33oorggs3tlivwgk3lfnz2esrc7ge) |
| __Build Requirements:__ | iOS 10 SDK, Xcode Version 8.2.x |
| __Runtime Requirements:__ | iOS 10 SDK |

AVAEMixerSample demonstrates playback, recording and mixing using AVAudioEngine.

\* Uses AVAudioFile and AVAudioPCMBuffer objects with a AVAudioPlayerNode to play audio. \* Creates an AVAudioSequencer to play MIDI files using the AVAudioUnitSampler instrument. \* Illustrates one-to-many connections (AVAudioConnectionPoint) using the connect:toConnectionPoints: API. \* Demonstrates connecting and applying effects using both the AVAudioUnitReverb and AVAudioUnitDistortion. \* Captures mixed or processed audio to a file via a node tap.

[Next](AVAEMixerSample-main.m.md)

