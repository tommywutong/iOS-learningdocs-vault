---
title: AVAudioSession - Audio Session APIs & The Remote IO Render Proc.
apple_id: DTS40012249
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-10-04'
source_url: https://developer.apple.com/library/archive/qa/qa1715/_index.html
archived_at: '2026-07-18T02:34:27.238118Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1715

# AVAudioSession - Audio Session APIs & The Remote IO Render Proc.

## Q:  Can I use AVAudioSession methods, property getters or the C based AudioSession APIs such as AudioSessionGetProperty to query for the Current Hardware Sample Rate in the Remote I/O render callback?

A: No, you should never do this. All Audio Session APIs can block and therefore should not be used for any reason in the render logic of the Remote I/O Audio Unit.

The render callback is called from a real-time thread and must return within a specific time-slice. Calling APIs that can potentially block, take a long time or take some indeterminate amount of time will adversely effect the render process causing clicks, skips or worse.

Operations such as synchronous file I/O, network I/O, any memory allocations, any Objective-C messaging (which can lead to the thread being paused), and of course APIs that can block the render thread must be avoided. Also note that most of the interaction with Core Foundation objects may be problematic because of the bridge between Core Foundation and the Objective-C runtime.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-10-04 | Updated for AVAudioSession |
| 2012-05-14 | New document that reinforces the point that all Audio Session APIs should never be used in the render logic of the Remote IO audio unit. |

