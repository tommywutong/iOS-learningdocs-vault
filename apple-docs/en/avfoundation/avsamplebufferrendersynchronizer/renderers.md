---
title: renderers
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/renderers
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/renderers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/renderers.json'
content_hash: 'sha256:10f2d2246c3feeff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# renderers

<sub>Instance Property</sub>

An array of queued sample buffer renderers currently attached to the synchronizer.

> [!warning] Deprecated
> Accessing non-Sendable renderers concurrently risks causing data races

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var renderers: [any AVQueuedSampleBufferRendering] { get }
```

## Discussion

This property includes all renderers that have been added to the synchronizer and haven’t been removed, including renderers that have been scheduled for removal, but have yet to be removed. This property is not KVO observable.

## See Also

### Managing renderers

- [- addRenderer:](<addrenderer(__).md>) — Adds a renderer to the list of renderers under the synchronizer’s control. _(deprecated)_
- [- removeRenderer:atTime:completionHandler:](<removerenderer(__at_completionhandler_).md>) — Removes a renderer from the synchronizer. _(deprecated)_
