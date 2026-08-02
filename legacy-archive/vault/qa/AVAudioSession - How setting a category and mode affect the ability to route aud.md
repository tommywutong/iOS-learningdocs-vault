---
title: AVAudioSession -  How setting a category and mode affect the ability to route
  audio to AirPlay
apple_id: DTS40013769
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-01-15'
source_url: https://developer.apple.com/library/archive/qa/qa1803/_index.html
archived_at: '2026-07-18T02:34:53.142170Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1803

# AVAudioSession - How setting a category and mode affect the ability to route audio to AirPlay

## Q:  How does an application's choice of audio category and mode affect the ability to route audio to AirPlay?

A: The `AVAudioSession` playback-only categories (`AVAudioSessionCategoryAmbient`, `AVAudioSessionCategorySoloAmbient` and `AVAudioSessionCategoryPlayback`) support both the __mirrored__ and __non-mirrored__ variants of AirPlay.

The `AVAudioSession` category `AVAudioSessionCategoryPlayAndRecord` supports only the __mirrored__ variant of AirPlay while the `AVAudioSessionCategoryMultiRoute` category does __not__ allow routing to AirPlay.

Modes modify the audio category in order to introduce specific tailored behavior. When an application uses the `AVAudioSessionModeVoiceChat` mode, AirPlay is __not__ allowed. The `AVAudioSessionModeVideoChat` mode introduced in iOS 7 supports the __mirrored__ variant of AirPlay.

Additionally, setting the `AVAudioSessionModeVoiceChat` mode will enable the `AVAudioSession` category option `AVAudioSessionCategoryOptionAllowBluetooth`, further modifying the behavior of the `AVAudioSessionCategoryPlayAndRecord` category to allow paired bluetooth hands-free profile (HFP) devices to be used for input and output.

Setting the `AVAudioSessionModeVideoChat` mode will further modify the behavior of the `AVAudioSessionCategoryPlayAndRecord` category by setting the `AVAudioSessionCategoryOptionAllowBluetooth` option and the `AVAudioSessionCategoryOptionDefaultToSpeaker` option.

See `AVAudioSession`.h for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-15 | Editorial |
| 2013-09-17 | New document that discusses how setting a AVAudioSession category and mode affect the ability to route audio to AirPlay. |

