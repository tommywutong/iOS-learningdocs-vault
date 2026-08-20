---
title: AVAudioSession - Differences between AVAudioSessionPortOverrideSpeaker and
  AVAudioSessionCategoryOptionDefaultToSpeaker Explained
apple_id: DTS40011281
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-09-11'
source_url: https://developer.apple.com/library/archive/qa/qa1754/_index.html
archived_at: '2026-07-18T02:34:35.703077Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1754

# AVAudioSession - Differences between AVAudioSessionPortOverrideSpeaker and AVAudioSessionCategoryOptionDefaultToSpeaker Explained

## Q:  Can you explain the difference between calling the AVAudioSession method `overrideOutputAudioPort:` with the value `AVAudioSessionPortOverrideSpeaker` and using the category option `AVAudioSessionCategoryOptionDefaultToSpeaker` with `setCategory:withOptions:error:`.

A: The difference is that setting the `AVAudioSessionPortOverride` by calling `overrideOutputAudioPort:` is more transient than using the category option `AVAudioSessionCategoryOptionDefaultToSpeaker`.

Calling `overrideOutputAudioPort:` and setting the `AVAudioSessionPortOverride` to `AVAudioSessionPortOverrideSpeaker` is a way of temporarily overriding the output to play to the speaker. Any route change or interruption will cause the audio to be routed back to its normal route, following the last-in wins rule. Think of using `overrideOutputAudioPort:` in terms of what you might use to implement a Speakerphone button where you want to be able to toggle between the speaker (`AVAudioSessionPortOverrideSpeaker`) and the normal output route (`AVAudioSessionPortOverrideNone`).

The preferred way to implement Speakerphone functionality is to use `MPVolumeView`'s Route button.

In contrast, `AVAudioSessionCategoryOptionDefaultToSpeaker` modifies the routing behavior of the `AVAudioSessionCategoryPlayAndRecord` category so that audio will __always__ route to the speaker rather than receiver if __no__ other accessory such as headphones are in use.

When using `AVAudioSessionCategoryOptionDefaultToSpeaker`, user gestures will be honored. For example, plugging in a headset will cause the route to change to headset mic/headphones and unplugging the headset will cause the route to change to built-in mic/speaker (as opposed to built-in mic/receiver) when this override has been set.

In the case of using a USB input-only accessory, audio input would come from the accessory and output would route to headphones (if attached) or speaker if headphones are not plugged in. The use case is simply to route audio to speaker instead of receiver in cases where the audio would normally go to the receiver. This option is a modifier for the category.

Route changes and interruptions will __not__ reset this override. Only changing the `AVAudioSession` category will cause this option to be reset.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-09-11 | Updated for AVAudioSession |
| 2011-09-20 | New document that discusses the difference between using the port override AVAudioSessionPortOverrideSpeaker and category option AVAudioSessionCategoryOptionDefaultToSpeaker. |

