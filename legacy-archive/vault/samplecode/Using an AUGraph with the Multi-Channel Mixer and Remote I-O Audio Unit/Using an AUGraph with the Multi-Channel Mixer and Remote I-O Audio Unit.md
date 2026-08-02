---
title: Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit
apple_id: TP40016060
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2015-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/iOSMultichannelMixerTest/Introduction/Intro.html
archived_at: '2026-07-18T03:29:35.860076Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2015-06-19 Updated for iOS 8 and Xcode 6.3.1. Removed CAStreamBasicDescription in favor of new AVAudioFormat and Common 32bit float format. |
| __Build Requirements:__ | iOS 8.3 SDK |
| __Runtime Requirements:__ | iPhone OS 8.3 or later |

Demonstrates how to build an Audio Unit Graph connecting a Multichannel Mixer instance to the RemoteIO unit. Two input busses are created each with input volume controls. An overall mixer output volume control is also provided and each bus may be enabled or disabled.

[Next](main.m.md)

