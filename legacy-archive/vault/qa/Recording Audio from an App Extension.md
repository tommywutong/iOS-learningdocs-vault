---
title: Recording Audio from an App Extension
apple_id: DTS40014885
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/qa/qa1872/_index.html
archived_at: '2026-07-18T02:35:11.878834Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1872

# Recording Audio from an App Extension

## Q:  Can I record audio from an app extension on iOS 8?

A: App extensions in iOS 8 are not allowed to record audio. There are a number of AudioToolbox framework functions and AVFoundation methods that will return errors (for example `AVAudioSessionErrorCodeCannotStartRecording`) if an app extension attempts to start recording audio.

Some examples of `AVFoundation` methods that will return errors if recording is attempted are:


```objc
AVAudioRecorder (see AVAudioRecorder.h)

- (BOOL)record;
- (BOOL)recordAtTime:(NSTimeInterval)time;
- (BOOL)recordForDuration:(NSTimeInterval) duration;
- (BOOL)recordAtTime:(NSTimeInterval)time forDuration:(NSTimeInterval) duration
```



```objc
AVAudioEngine (see AVAudioEngine.h) in cases where the inputNode object is used.

- (BOOL)startAndReturnError:(NSError **)outError;
```

Some examples of `AudioToolbox` functions that will return errors if recording is attempted are:


```
AudioQueueStart() (see AudioQueue.h) when used with an AudioQueue object created by a call to AudioQueueNewInput().

AUGraphStart() (see AUGraph.h) or AudioOutputUnitStart() (see AudioOutputUnit.h) if the input element on the Remote I/O (kAudioUnitSubType_RemoteIO) or Voice Processing (kAudioUnitSubType_VoiceProcessingIO) audio unit has been enabled.
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-14 | New document that discusses audio recording from an App Extension. |

