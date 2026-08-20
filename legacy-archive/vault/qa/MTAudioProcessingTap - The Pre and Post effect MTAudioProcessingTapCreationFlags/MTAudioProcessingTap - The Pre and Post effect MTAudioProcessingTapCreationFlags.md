---
title: MTAudioProcessingTap - The Pre and Post effect MTAudioProcessingTapCreationFlags
apple_id: DTS40013184
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-03-11'
source_url: https://developer.apple.com/library/archive/qa/qa1783/_index.html
archived_at: '2026-07-18T02:34:43.910472Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1783

# MTAudioProcessingTap - The Pre and Post effect MTAudioProcessingTapCreationFlags

## Q:  `MTAudioProcessingTapCreate` allows you to pass in some `MTAudioProcessingTapCreationFlags` flags designating if you want the tap inserted Pre or Post Effect. What does this mean?

A: The `MTAudioProcessingTap` object is always used with a `AVAudioMix` object and its array of instances of `AVAudioMixInputParameters`. You associate a  `MTAudioProcessingTapRef`  with a track using the `AVMutableAudioMixInputParameters` `audioTapProcessor` property as shown in Figure 1.

__Figure 1__  MTAudioProcessingTap associated with AVAudioMixInputParameters.

!

When you create a "pre-effects" audio tap using the `kMTAudioProcessingTapCreationFlag_PreEffects` flag, the tap will be called before any effects specified by `AVAudioMixInputParameters` are applied; when you create a "post-effects" tap by using the `kMTAudioProcessingTapCreationFlag_PostEffects` flag, the tap will be called after those effects are applied. Currently the only "effect" that `AVAudioMixInputParameters` supports is a linear volume ramp.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-03-11 | New document that discusses the flags used when creating audio processing taps. |

