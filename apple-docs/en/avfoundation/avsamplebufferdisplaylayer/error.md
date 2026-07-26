---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.10+（15.0 起废弃）, tvOS 10.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/error.json'
content_hash: 'sha256:eca8a90647b940b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# error

<sub>Instance Property</sub>

The error that caused the failure.

> [!warning] Deprecated
> Use [error](../avsamplebuffervideorenderer/error.md) on [sampleBufferRenderer](samplebufferrenderer.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The value of this property is an `NSError` that describes what caused the display layer to no longer be able to enqueue sample buffers. If the status is not [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md), the value of this property is `nil`.
