---
title: 'init(postProcessingAsVideoLayers:in:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayers:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayers:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool/init%28postprocessingasvideolayers%3Ain%3A%29.json'
content_hash: 'sha256:6cb832f710f05ea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionCoreAnimationTool](../avvideocompositioncoreanimationtool.md)

# init(postProcessingAsVideoLayers:in:)

<sub>Initializer</sub>

Composes the composited video frames with the Core Animation layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], in animationLayer: CALayer)
```

## Parameters

- `videoLayers` — An array containing the video layers

- `animationLayer` — The animation layer.

## Return Value

A new `AVVideoCompositionCoreAnimationTool` instance with the composited video frames and the rendered animation layer.

## Discussion

Duplicates the composited video frames in each videoLayer and renders animationLayer to produce the final frame. The `videoLayers` should be in `animationLayer`’s sublayer tree.

The `animationLayer` should not come from, or be added to, another layer tree.

> [!note] Note
> On iOS, a layer instance backing a [UIView](../../uikit/uiview.md) usually have their content flipped, as defined by the [contentsAreFlipped()](<../../quartzcore/calayer/contentsareflipped().md>) method. It may be required to insert a [CALayer](../../quartzcore/calayer.md) instance with its [isGeometryFlipped](../../quartzcore/calayer/isgeometryflipped.md) property set to [true](../../swift/true.md) in the layer hierarchy to get the same result when attaching a layer to the receiver when the layer backs a [UIView](../../uikit/uiview.md).

## See Also

### Creating a composition tool

- [+ videoCompositionCoreAnimationToolWithAdditionalLayer:asTrackID:](<init(additionallayer_astrackid_).md>) — Adds a Core Animation layer to the video composition.
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:inLayer:](<init(postprocessingasvideolayer_in_).md>) — Composes the composited video frame with a Core Animation layer. _(deprecated)_
- [init(configuration:)](<init(configuration_).md>) — Compose the composited video frames with the Core Animation layer.
- [Configuration](configuration.md) — Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.
