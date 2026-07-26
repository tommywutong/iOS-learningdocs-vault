---
title: AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification.json'
content_hash: 'sha256:469507fb1b3aecf5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification

<sub>Global Variable</sub>

A notification the system posts when a sample buffer display layer changes its decoding requirements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSNotificationName const AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification;
```

## See Also

### Notifications

- [AVSampleBufferAudioRendererOutputConfigurationDidChangeNotification](avsamplebufferaudiorendereroutputconfigurationdidchangenotification.md) — A notification that indicates the hardware configuration does not match the enqueued data format.
- [AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification](avsamplebufferaudiorendererwasflushedautomaticallynotification.md) — A notification that fires whenever the receiver’s enqueued media data has been flushed for a reason other than a call to the -flush method.
- [AVSampleBufferDisplayLayerOutputObscuredDueToInsufficientExternalProtectionDidChangeNotification](avsamplebufferdisplaylayeroutputobscuredduetoinsufficientexternalprotectiondidchangenotification.md)
- [AVSampleBufferDisplayLayerReadyForDisplayDidChangeNotification](avsamplebufferdisplaylayerreadyfordisplaydidchangenotification.md)
