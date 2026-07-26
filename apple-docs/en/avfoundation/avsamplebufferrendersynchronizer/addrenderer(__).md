---
title: 'addRenderer(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/addrenderer(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/addrenderer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/addrenderer%28_%3A%29.json'
content_hash: 'sha256:5de2724c5dff8347'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# addRenderer(_:)

<sub>Instance Method</sub>

Adds a renderer to the list of renderers under the synchronizer’s control.

> [!warning] Deprecated
> Get an AVQueuedSampleBufferRenderingReceiver from an audio or video renderer with sampleBufferReceiver() and add it to the synchronizer with addReceiver(_:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addRenderer(_ renderer: any AVQueuedSampleBufferRendering)
```

## Parameters

- `renderer` — The render to be added.

## Discussion

This method can be called while [rate](rate.md) is not `0.0`.

## See Also

### Managing renderers

- [renderers](renderers.md) — An array of queued sample buffer renderers currently attached to the synchronizer. _(deprecated)_
- [- removeRenderer:atTime:completionHandler:](<removerenderer(__at_completionhandler_).md>) — Removes a renderer from the synchronizer. _(deprecated)_
