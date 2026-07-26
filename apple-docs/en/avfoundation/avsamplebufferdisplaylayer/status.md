---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.10+（15.0 起废弃）, tvOS 10.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/status
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/status'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/status.json'
content_hash: 'sha256:aa62fe5e4b38d0c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# status

<sub>Instance Property</sub>

The ability of the display layer to be used for enqueuing sample buffers.

> [!warning] Deprecated
> Use sampleBufferRenderer's status instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var status: AVQueuedSampleBufferRenderingStatus { get }
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [status](../avsamplebuffervideorenderer/status.md) on [sampleBufferRenderer](samplebufferrenderer.md) instead.

The value of this property is an [AVQueuedSampleBufferRenderingStatus](../avqueuedsamplebufferrenderingstatus.md) that indicates whether the receiver can be used for enqueuing sample buffers.

When the value of this property is [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md), the receiver can no longer be used and a new instance needs to be created in its place. When this happens, clients can check the value of the [error](error.md) property to determine the failure.

This property supports key-value observing.

## See Also

### Getting display layer settings

- [AVQueuedSampleBufferRenderingStatus](../avqueuedsamplebufferrenderingstatus.md) — The statuses for sample buffer rendering. _(deprecated)_
