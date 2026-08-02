---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/History/History.html
archived_at: '2026-07-18T02:59:58.274016Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Previous](LICENSE.txt.md)

# Document Revision History

This table describes the changes to _Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)_.

| __Date__ | __Notes__ |
| 2017-03-23 | handleMediaServicesReset now configures AVAudioSession per QA1749 |
| 2017-02-16 | (new) Audio parameter views on iPhone now have a 'Dismiss' button in addition to 'Swipe down' to dismiss. (modified) AVAudioEngine is now paused when nothing is playing or being recorded. (modified) Refactored some methods to support pausing and to ensure proper initialization after reset or engine reconfiguration. |
| 2017-01-12 | Explicitly use the buffer format as the connection format for the player to reverb & reverb to mainMixer, to make it clear that these formats must match. Project updated for Xcode 8.2.1. |
| 2016-01-08 | Updated for iOS 9 and Xcode 7 |
| 2015-06-25 | Improved handling of audio interruptions, added audio key to the UIBackgroundModes, audio category changed to Playback from PlayAndRecord. Fixed a bug in handleMediaServicesReset: |
| 2015-03-09 | First public release. |

[Previous](LICENSE.txt.md)

