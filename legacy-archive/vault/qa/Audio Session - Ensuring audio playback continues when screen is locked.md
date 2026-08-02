---
title: Audio Session - Ensuring audio playback continues when screen is locked
apple_id: DTS40008064
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2009-09-16'
source_url: https://developer.apple.com/library/archive/qa/qa1626/_index.html
archived_at: '2026-07-18T02:33:00.560785Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1626

# Audio Session - Ensuring audio playback continues when screen is locked

## Q:  How can I ensure my application continues to play audio when the device is locked?

A: How can I ensure my application continues to play audio when the device is locked?

Starting with iPhone OS 2.2, applications using the default audio session will no longer play audio when the screen is locked by the user or after the Auto-Lock period expires.

If your application needs to play audio while the screen is locked, you must now explicitly set the audio session category to `kAudioSessionCategory_MediaPlayback`. This is because, with the release of iPhone OS 2.2, the default audio session playback category has been changed from `kAudioSessionCategory_MediaPlayback` to `kAudioSessionCategory_SoloAmbientSound`.

As discussed in the Audio Session Programming Guide, you must initialize, configure, and explicitly use your audio session to enable your application to respond to interruptions and audio route changes. Additionally, the default audio session playback category may not be best for your application. Apple recommends that you explicitly initialize and set up your application's audio session to fit your application's requirements.

Listing 1 demonstrates the use of the Audio Session APIs to initialize and explicitly set the category to `kAudioSessionCategory_MediaPlayback` ensuring audio playback when locked.

__Listing 1__

```
{  ...  // initialize the audio session object for this application, // registering the callback Audio Session Services will invoke when there's an interruption AudioSessionInitialize(NULL, kCFRunLoopDefaultMode, myInterruptionListenerCallback, self);  // register a property listener so we're notified when there's a route change AudioSessionAddPropertyListener(kAudioSessionProperty_AudioRouteChange,                                 myAudioRouteChangeListenerCallback, self);  // set the audio session category - kAudioSessionCategory_MediaPlayback // will ensure our audio playback continues when the device is locked UInt32 sessionCategory = kAudioSessionCategory_MediaPlayback; AudioSessionSetProperty(kAudioSessionProperty_AudioCategory, sizeof(sessionCategory), &sessionCategory);  ...  // activate the audio session immmediately before playback starts AudioSessionSetActive(true);  ...  }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-09-16 | Editorial |
| 2008-10-24 | New document that discusses how to ensure audio playback while the phone is locked. |

