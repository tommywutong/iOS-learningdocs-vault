---
title: 'init(postProcessingAsVideoLayer:in:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayer:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayer:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool/init%28postprocessingasvideolayer%3Ain%3A%29.json'
content_hash: 'sha256:a6ad4ee33904b0c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionCoreAnimationTool](../avvideocompositioncoreanimationtool.md)

# init(postProcessingAsVideoLayer:in:)

<sub>Initializer</sub>

Composes the composited video frame with a Core Animation layer.

> [!warning] Deprecated
> Use .init(configuration: AVVideoCompositionCoreAnimationTool.Configuration) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(postProcessingAsVideoLayer videoLayer: CALayer, in animationLayer: CALayer)
```

## Parameters

- `videoLayer` — A video layer.

- `animationLayer` — An animation layer.

## Return Value

A new animation tool for the composition.

## Discussion

Place composited video frames in `videoLayer` and render `animationLayer` to produce the final frame.

The `videoLayer` should be in the `animationLayer` sublayer tree. The `animationLayer` should not come from, or be added to, another layer tree.

## See Also

### Creating a composition tool

- [+ videoCompositionCoreAnimationToolWithAdditionalLayer:asTrackID:](<init(additionallayer_astrackid_).md>) — Adds a Core Animation layer to the video composition.
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:](<init(postprocessingasvideolayers_in_).md>) — Composes the composited video frames with the Core Animation layer.
- [init(configuration:)](<init(configuration_).md>) — Compose the composited video frames with the Core Animation layer.
- [Configuration](configuration.md) — Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.
