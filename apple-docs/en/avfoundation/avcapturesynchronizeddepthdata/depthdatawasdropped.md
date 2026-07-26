---
title: depthDataWasDropped
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizeddepthdata/depthdatawasdropped
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata/depthdatawasdropped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddepthdata/depthdatawasdropped.json'
content_hash: 'sha256:cbe1d9758eb4da79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedDepthData](../avcapturesynchronizeddepthdata.md)

# depthDataWasDropped

<sub>Instance Property</sub>

A Boolean value indicating whether depth data was discarded between capture and processing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var depthDataWasDropped: Bool { get }
```

## Discussion

If this value is [true](../../swift/true.md), depth data was captured for this synchronization point but could not be delivered. This situation differs from that where no depth data capture for the synchronization timestamp occurs. In that case, there is no [AVCaptureSynchronizedDepthData](../avcapturesynchronizeddepthdata.md) object present in the [AVCaptureSynchronizedDataCollection](../avcapturesynchronizeddatacollection.md) object delivered to your delegate method.

## See Also

### Handling dropped data

- [droppedReason](droppedreason.md) — A value indicating why the capture output failed to deliver depth data, if applicable.
