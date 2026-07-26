---
title: AVSampleBufferDisplayLayerFailedToDecodeNotification
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 10.2+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayerfailedtodecodenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayerfailedtodecodenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayerfailedtodecodenotification.json'
content_hash: 'sha256:634da5be76e9fe22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferDisplayLayerFailedToDecodeNotification

<sub>Global Variable</sub>

A notification the system posts when a sample buffer display layer fails to decode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const AVSampleBufferDisplayLayerFailedToDecodeNotification;
```

## Discussion

You can retrieve the error object from the user information dictionary by querying it for its [AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey](avsamplebufferdisplaylayerfailedtodecodenotificationerrorkey.md) value.

## See Also

### Handling errors

- [AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey](avsamplebufferdisplaylayerfailedtodecodenotificationerrorkey.md) — The key for the corresponding error.
