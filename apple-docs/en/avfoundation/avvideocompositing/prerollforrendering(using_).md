---
title: 'prerollForRendering(using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositing/prerollforrendering(using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/prerollforrendering(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/prerollforrendering%28using%3A%29.json'
content_hash: 'sha256:1ec9d32abd6e4cdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# prerollForRendering(using:)

<sub>Instance Method</sub>

Tells a custom video compositor to perform any work in the prerolling phase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func prerollForRendering(using renderHint: AVVideoCompositionRenderHint)
```

## Parameters

- `renderHint` — Information about the upcoming composition requests.

## Discussion

The AVFoundation framework may perform prerolling to load media data to prime the render pipelines for smoother playback. This method is called in the prerolling phase so that the compositor can load composition resources, such as overlay images, that will be needed as soon as the playback starts.

Not all rendering scenarios use prerolling. For example, this method won’t be called during seeking.

If this method is called, it is guaranteed to be invoked before the first [- startVideoCompositionRequest:](<startrequest(__).md>) call.

This method is synchronous. The prerolling won’t finish until the method returns.

## See Also

### Preparing to render frames

- [- anticipateRenderingUsingHint:](<anticipaterendering(using_).md>) — Informs a custom video compositor about upcoming rendering requests.
- [AVVideoCompositionRenderHint](../avvideocompositionrenderhint.md) — Information about upcoming composition requests, such as composition start time and end time.
