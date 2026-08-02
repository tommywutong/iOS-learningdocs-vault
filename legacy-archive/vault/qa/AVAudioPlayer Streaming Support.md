---
title: AVAudioPlayer Streaming Support
apple_id: DTS40008185
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-04-04'
source_url: https://developer.apple.com/library/archive/qa/qa1634/_index.html
archived_at: '2026-07-18T02:33:02.694857Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1634

# AVAudioPlayer Streaming Support

## Q:  Does the `AVAudioPlayer` provide support for streaming audio content?

A: The `AVAudioPlayer` class does not provide support for streaming audio based on HTTP URL's. The URL used with `initWithContentsOfURL:` must be a File URL (`file://`). That is, a local path.

As mentioned in [Core Audio Essentials](https://developer.apple.com/library/ios/#documentation/MusicAudio/Conceptual/CoreAudioOverview/CoreAudioEssentials/CoreAudioEssentials.html#//apple_ref/doc/uid/TP40003577-CH10-SW1), the `AVAudioPlayer` class is ideal for applications that require a simple Objective-C interface for audio playback, are not concerned about audio positioning or precise synchronization, and are not playing audio from a network stream.

To play streamed audio, connect to a network stream using the `CFNetwork` interfaces from Core Foundation, such as those in `CFHTTPMessage`. Parse the network packets into audio packets using Audio File Stream Services (`AudioToolbox/AudioFileStream.h`) and play the audio packets using Audio Queue Services (`AudioToolbox/AudioQueue.h`). You may also use Audio File Stream Services to parse audio packets from an on-disk file.

`AVPlayer` (available in iOS 4.0 and later) may also be used to stream audio content.

A sample called `AudioFileStreamExample` demonstrates the use of Audio File Stream APIs and can be found in the Mac OS X Reference Library.

[SpeakHere](https://developer.apple.com/iphone/library/samplecode/SpeakHere/index.html) - Demonstrates Audio Queue Services.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-04-04 | Editorial |
| 2011-06-28 | Editorial |
| 2009-09-16 | Editorial |
| 2009-01-29 | New document that Discusses AVAudioPlayer and support for streaming audio. |

