---
title: timestamp
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizeddata/timestamp
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddata/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddata/timestamp.json'
content_hash: 'sha256:5bf1397b53121d99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedData](../avcapturesynchronizeddata.md)

# timestamp

<sub>Instance Property</sub>

The time at which this synchronized data was captured.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var timestamp: CMTime { get }
```

## Discussion

Synchronized data is always synchronized to the [masterClock](../avcapturesession/masterclock.md) time of the [AVCaptureSession](../avcapturesession.md) object to which the data output is connected.
