---
title: 'removeRenderer(_:at:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/removerenderer(_:at:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/removerenderer(_:at:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/removerenderer%28_%3Aat%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:0021211498602531'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# removeRenderer(_:at:completionHandler:)

<sub>Instance Method</sub>

Removes a renderer from the synchronizer.

> [!warning] Deprecated
> Use removeReceiver(_:at:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeRenderer(_ renderer: any AVQueuedSampleBufferRendering, at time: CMTime, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeRenderer(_ renderer: any AVQueuedSampleBufferRendering, at time: CMTime) async -> Bool
```

## Parameters

- `renderer` — 

- `time` — The time on the timebase’s timeline at which the renderer should be removed. If the time is in the past, the renderer is immediately removed.

- `completionHandler` — An optional block to invoke when the renderer is removed from the synchronizer. The block takes one argument: - **didRemoveRenderer** — A Boolean value indicating the whether the renderer was removed.

## Discussion

This method removes the renderer asynchronously. The method can be called more than once, with a subsequent scheduled removal replacing a previously scheduled removal. This method can be called while [rate](rate.md) is not `0.0`.

Clients may provide an optional `completionHandler` to be notified when the scheduled removal is complete. If provided, the completion handler will always be called with the following values for `didRemoveRenderer`:

- If the renderer has not been added to this synchronizer, `didRemoveRenderer` is `NO`.
- If the removal of a particular renderer is scheduled after the same renderer’s removal was previous scheduled but not yet occurred, the previously scheduled removal’s completion handler is and `didRemoveRenderer` set to `NO`.
- When the renderer is removed due to a scheduled removal, the completion handler is called and `didRemoveRenderer` set to YES.

## See Also

### Managing renderers

- [renderers](renderers.md) — An array of queued sample buffer renderers currently attached to the synchronizer. _(deprecated)_
- [- addRenderer:](<addrenderer(__).md>) — Adds a renderer to the list of renderers under the synchronizer’s control. _(deprecated)_
