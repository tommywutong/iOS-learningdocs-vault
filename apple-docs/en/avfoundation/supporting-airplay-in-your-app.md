---
title: Supporting AirPlay in your app
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/supporting-airplay-in-your-app
source_url: 'https://developer.apple.com/documentation/avfoundation/supporting-airplay-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/supporting-airplay-in-your-app.json'
content_hash: 'sha256:de372381e77b32de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Streaming and AirPlay](streaming-and-airplay.md)

# Supporting AirPlay in your app

<sub>Article</sub>

Set up your app to use AirPlay to send content wirelessly.

## Overview

AirPlay enables you to send content wirelessly from an Apple device to an Apple TV or AirPlay-enabled speaker. AirPlay provides enhanced support for wireless audio distribution, including the ability to send content to multiple AirPlay-enabled speakers.

### Identify the audio type the app plays

In iOS, tvOS, and watchOS, set your audio session’s route-sharing policy to `.longForm`. Long-form audio is anything other than system sounds, such as music, audiobooks, or podcasts. This setting identifies the audio that an app plays, such as in the following example.

```swift
let audioSession = AVAudioSession.sharedInstance()
try audioSession.setCategory(.playback, 
                             mode: .default, 
                             policy: .longFormAudio)
```

### Add an AirPlay picker

Add [AVRoutePickerView](../avkit/avroutepickerview.md) to your view hierarchy to include an AirPlay picker in your app. The picker provides users with a list of potential AirPlay devices they can use with your app. To control when to show the picker, use [AVRouteDetector](avroutedetector.md) to identify the state of the route detector.

### Add a media player

Use APIs to customize your AirPlay adoption with Media Player integration. If you use [MPRemoteCommandCenter](../mediaplayer/mpremotecommandcenter.md), you can receive remote commands. If you use [MPNowPlayingInfoCenter](../mediaplayer/mpnowplayinginfocenter.md), you can inform the system metadata about the track that’s playing on the device.

### Configure an app for fast streaming

Adopt one of two playback API sets that take advantage of the enhanced buffering in AirPlay:

- For simple enhanced buffering, use [AVPlayer](avplayer.md) or [AVQueuePlayer](avqueueplayer.md). This works well for video content. For more information, see [Implementing simple enhanced buffering for your content](implementing-simple-enhanced-buffering-for-your-content.md).
- For more flexibility with enhanced buffering, use [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) and [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md). This option is better for apps that require control over I/O, perform preprocessing on their media data, or have a DRM model that [AVPlayer](avplayer.md) doesn’t support. For more information, see [Implementing flexible enhanced buffering for your content](implementing-flexible-enhanced-buffering-for-your-content.md).
