---
title: 'anticipateRendering(using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositing/anticipaterendering(using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/anticipaterendering(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/anticipaterendering%28using%3A%29.json'
content_hash: 'sha256:6cb7af51fc9a9cd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# anticipateRendering(using:)

<sub>Instance Method</sub>

Informs a custom video compositor about upcoming rendering requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func anticipateRendering(using renderHint: AVVideoCompositionRenderHint)
```

## Parameters

- `renderHint` — Information about the upcoming composition requests.

## Discussion

In this method, the compositor can load composition resources, such as overlay images, that will be needed in the anticipated rendering time range.

Unlike the [- startVideoCompositionRequest:](<startrequest(__).md>) method, which is invoked only when the frame compositing is necessary, this method is typically called every frame duration. It allows the custom compositor to load and unload a composition resource such as overlay images at an appropriate time.

In forward playback, the render hint’s [startCompositionTime](../avvideocompositionrenderhint/startcompositiontime.md) is less than its [endCompositionTime](../avvideocompositionrenderhint/endcompositiontime.md). In reverse playback, its [endCompositionTime](../avvideocompositionrenderhint/endcompositiontime.md) is less than its [startCompositionTime](../avvideocompositionrenderhint/startcompositiontime.md). For seeking, the two values are equivalent, which means the upcoming composition request time range is unknown.

This method is guaranteed to be called before [- startVideoCompositionRequest:](<startrequest(__).md>) for a given composition time.

This method is synchronous. Make sure that your implementation returns quickly to ensure that playback doesn’t stall and cause frame drops.

## See Also

### Preparing to render frames

- [- prerollForRenderingUsingHint:](<prerollforrendering(using_).md>) — Tells a custom video compositor to perform any work in the prerolling phase.
- [AVVideoCompositionRenderHint](../avvideocompositionrenderhint.md) — Information about upcoming composition requests, such as composition start time and end time.
