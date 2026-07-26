---
title: depthData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizeddepthdata/depthdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddepthdata/depthdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddepthdata/depthdata.json'
content_hash: 'sha256:f28e731d5e025d27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedDepthData](../avcapturesynchronizeddepthdata.md)

# depthData

<sub>Instance Property</sub>

The depth data captured at this synchronization point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var depthData: AVDepthData { get }
```

## Discussion

If the [depthDataWasDropped](depthdatawasdropped.md) property is [true](../../swift/true.md), this [AVDepthData](../avdepthdata.md) object does not contain a depth map (instead, it contains only metadata).

This value is equivalent to that provided by the [- depthDataOutput:didOutputDepthData:timestamp:connection:](<../avcapturedepthdataoutputdelegate/depthdataoutput(__didoutput_timestamp_connection_).md>) or [- depthDataOutput:didDropDepthData:timestamp:connection:reason:](<../avcapturedepthdataoutputdelegate/depthdataoutput(__diddrop_timestamp_connection_reason_).md>) delegate method when using a depth capture output without a data output synchronizer.
