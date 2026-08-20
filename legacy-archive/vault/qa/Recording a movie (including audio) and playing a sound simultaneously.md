---
title: Recording a movie (including audio) and playing a sound simultaneously
apple_id: DTS40013121
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-02-19'
source_url: https://developer.apple.com/library/archive/qa/qa1566/_index.html
archived_at: '2026-07-18T02:32:18.519538Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1566

# Recording a movie (including audio) and playing a sound simultaneously

## Q:  How do I record a movie (including audio) and play a sound simultaneously?

A: To allow recording and playback of audio, set your audio session category to `AVAudioSessionCategoryPlayAndRecord`.

To play recorded movie audio along with your own sounds, you must use a mixable category configuration for your audio session. You can override the non-mixing characteristic of the `AVAudioSessionCategoryPlayAndRecord` category by applying the `kAudioSessionProperty_OverrideCategoryMixWithOthers` property to your audio session.

Here's a code snippet:

__Listing 1__  Setting your audio session category for simultaneous playback/record and mixing.

```
NSError *setCategoryError = nil;

/* Set the audio session category to allow for playback/recording and mixing */
BOOL setCategorySuccess = [[AVAudioSession sharedInstance]
                                     setCategory:AVAudioSessionCategoryPlayAndRecord
                                     withOptions: AVAudioSessionCategoryOptionMixWithOthers
                                     error:&setCategoryError];

if (setCategorySuccess == NO) { /* handle error here */ }


NSError *activationError = nil;

/* Activate the audio session */
BOOL activationResult = [[AVAudioSession sharedInstance] setActive: YES
                                              error: &activationError];

if (activationResult == NO) { /* handle the error here */ }
```

See the section "Modifying Playback Mixing Behavior" in the [Audio Session Programming Guide](https://developer.apple.com/library/ios/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/AudioSessionProgrammingGuide.pdf) for more information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-02-19 | New document that shows how to record a movie (including audio) and play a sound simultaneously |

