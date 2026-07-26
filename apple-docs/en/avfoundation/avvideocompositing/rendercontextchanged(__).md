---
title: 'renderContextChanged(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositing/rendercontextchanged(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/rendercontextchanged(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/rendercontextchanged%28_%3A%29.json'
content_hash: 'sha256:56b0789817269fe3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# renderContextChanged(_:)

<sub>Instance Method</sub>

Tells the compositor that the composition changed render contexts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext)
```

## Parameters

- `newRenderContext` — The new render context of the video composition.

## See Also

### Observing render context changes

- [AVVideoCompositionRenderContext](../avvideocompositionrendercontext.md) — An object that defines the context in which custom compositors render pixel buffers.
