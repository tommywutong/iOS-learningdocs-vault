---
title: customVideoCompositor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/customvideocompositor
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/customvideocompositor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/customvideocompositor.json'
content_hash: 'sha256:adf7ac3ed33651a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# customVideoCompositor

<sub>Instance Property</sub>

The custom video compositor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated var customVideoCompositor: (any AVVideoCompositing)? { get }
```

## Discussion

The custom video compositor instance that is used during image generation is accessible via this property after the value of [videoComposition](videocomposition.md) is set to an [AVVideoComposition](../avvideocomposition.md) instance that specifies a custom video compositor class. Any additional communication between the application and that instance of the custom video compositor, if any is required for configuration or other purposes, can only occur once that has happened.

If the value of [videoComposition](videocomposition.md) is changed from an [AVVideoComposition](../avvideocomposition.md) that specifies a custom video compositor class to another instance of [AVVideoComposition](../avvideocomposition.md) that specifies the same custom video compositor class, the instance of the custom video compositor that was previously created will receive the [- renderContextChanged:](<../avvideocompositing/rendercontextchanged(__).md>) message and remain in use for subsequent image generation.

This property is `nil` if there is no video compositor, or if the internal video compositor is in use.

## See Also

### Configuring video compositing

- [videoComposition](videocomposition.md) — The video composition settings to be applied during playback.
- [seekingWaitsForVideoCompositionRendering](seekingwaitsforvideocompositionrendering.md) — A Boolean value that indicates whether the item’s timing follows the displayed video frame when seeking with a video composition.
