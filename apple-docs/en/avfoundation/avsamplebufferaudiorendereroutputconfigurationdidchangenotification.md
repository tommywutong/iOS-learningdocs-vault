---
title: AVSampleBufferAudioRendererOutputConfigurationDidChangeNotification
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorendereroutputconfigurationdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorendereroutputconfigurationdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorendereroutputconfigurationdidchangenotification.json'
content_hash: 'sha256:c12df4578a4563b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferAudioRendererOutputConfigurationDidChangeNotification

<sub>Global Variable</sub>

A notification that indicates the hardware configuration does not match the enqueued data format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSNotificationName const AVSampleBufferAudioRendererOutputConfigurationDidChangeNotification;
```

## Discussion

The output configuration of the playback hardware might change during the playback session if other clients play content with different format. In such cases, if the media content format does not match the hardware configuration it would produce suboptimal rendering of the enqueued media data. When the framework detects such mismatch it will issue this notification, so the client can flush the renderer and re-enqueue the sample buffers from the current media playhead, which will configure the hardware based on the format of newly enqueued sample buffers.

## See Also

### Notifications

- [AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification](avsamplebufferaudiorendererwasflushedautomaticallynotification.md) — A notification that fires whenever the receiver’s enqueued media data has been flushed for a reason other than a call to the -flush method.
- [AVSampleBufferDisplayLayerOutputObscuredDueToInsufficientExternalProtectionDidChangeNotification](avsamplebufferdisplaylayeroutputobscuredduetoinsufficientexternalprotectiondidchangenotification.md)
- [AVSampleBufferDisplayLayerReadyForDisplayDidChangeNotification](avsamplebufferdisplaylayerreadyfordisplaydidchangenotification.md)
- [AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification](avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification.md) — A notification the system posts when a sample buffer display layer changes its decoding requirements.
