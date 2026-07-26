---
title: AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorendererwasflushedautomaticallynotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorendererwasflushedautomaticallynotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorendererwasflushedautomaticallynotification.json'
content_hash: 'sha256:5679763aeb6e421b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification

<sub>Global Variable</sub>

A notification that fires whenever the receiver’s enqueued media data has been flushed for a reason other than a call to the -flush method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSNotificationName const AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification;
```

## Discussion

The renderer may flush enqueued media data when the user routes playback to a new destination. The renderer may also flush enqueued media data when the playback rate of the attached AVSampleBufferRenderSynchronizer is changed (e.g. 1.0 -\> 2.0 or 1.0 -\> 0.0 -\> 2.0), however no flush will occur for normal pauses (non-zero -\> 0.0) and resumes (0.0 -\> same non-zero rate as before).

When an automatic flush occurs, the attached render synchronizer’s timebase will remain running at its current rate. It is typically best to respond to this notification by enqueueing media data with timestamps starting at the timebase’s current time. To the listener, this will sound similar to muting the audio for a short period of time. If it is more desirable to ensure that all audio is played than to keep the timeline moving, you may also stop the synchronizer, set the synchronizer’s current time to the value of AVSampleBufferAudioRendererFlushTimeKey, start reenqueueing sample buffers with timestamps starting at that time, and restart the synchronizer. To the listener, this will sound similar to pausing the audio for a short period of time.

This notification is delivered on an arbitrary thread. If sample buffers are being enqueued with the renderer concurrently with the receipt of this notification, it is possible that one or more sample buffers will remain enqueued in the renderer. This is generally undesirable, because the sample buffers that remain will likely have timestamps far ahead of the timebase’s current time and so won’t be rendered for some time. The best practice is to invoke the -flush method, in a manner that is serialized with enqueueing sample buffers, after receiving this notification and before resuming the enqueueing of sample buffers.

## See Also

### Notifications

- [AVSampleBufferAudioRendererOutputConfigurationDidChangeNotification](avsamplebufferaudiorendereroutputconfigurationdidchangenotification.md) — A notification that indicates the hardware configuration does not match the enqueued data format.
- [AVSampleBufferDisplayLayerOutputObscuredDueToInsufficientExternalProtectionDidChangeNotification](avsamplebufferdisplaylayeroutputobscuredduetoinsufficientexternalprotectiondidchangenotification.md)
- [AVSampleBufferDisplayLayerReadyForDisplayDidChangeNotification](avsamplebufferdisplaylayerreadyfordisplaydidchangenotification.md)
- [AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification](avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification.md) — A notification the system posts when a sample buffer display layer changes its decoding requirements.
