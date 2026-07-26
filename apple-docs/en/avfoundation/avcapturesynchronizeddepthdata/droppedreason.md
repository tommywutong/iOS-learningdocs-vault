---
title: droppedReason
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizeddepthdata/droppedreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata/droppedreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddepthdata/droppedreason.json'
content_hash: 'sha256:6a33b921e6f5f37b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedDepthData](../avcapturesynchronizeddepthdata.md)

# droppedReason

<sub>Instance Property</sub>

A value indicating why the capture output failed to deliver depth data, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var droppedReason: AVCaptureOutput.DataDroppedReason { get }
```

## See Also

### Handling dropped data

- [depthDataWasDropped](depthdatawasdropped.md) — A Boolean value indicating whether depth data was discarded between capture and processing.
