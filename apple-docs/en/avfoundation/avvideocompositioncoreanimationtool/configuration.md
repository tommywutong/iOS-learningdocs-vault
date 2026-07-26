---
title: AVVideoCompositionCoreAnimationTool.Configuration
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioncoreanimationtool/configuration
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration.json'
content_hash: 'sha256:0a9b893df6df6b3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionCoreAnimationTool](../avvideocompositioncoreanimationtool.md)

# AVVideoCompositionCoreAnimationTool.Configuration

<sub>Structure</sub>

Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Configuration
```

## Topics

### Creating a configuration

- [init(postProcessingAsVideoLayer:containingLayer:)](<configuration/init(postprocessingasvideolayer_containinglayer_).md>) — Place composited video frames in videoLayer and render animationLayer to produce the final frame. Normally videoLayer should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.
- [init(postProcessingAsVideoLayers:containingLayer:)](<configuration/init(postprocessingasvideolayers_containinglayer_).md>) — Duplicate the composited video frames in each videoLayer and render animationLayer to produce the final frame. Normally videoLayers should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.

### Inspecting the configuration

- [containingLayer](configuration/containinglayer.md) — Containing layer to be rendered into, producing the final frame.
- [layers](configuration/layers.md) — Layer(s) to contain the composited video frames. Frames are duplicated if there is more than one layer.

## See Also

### Creating a composition tool

- [+ videoCompositionCoreAnimationToolWithAdditionalLayer:asTrackID:](<init(additionallayer_astrackid_).md>) — Adds a Core Animation layer to the video composition.
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:inLayer:](<init(postprocessingasvideolayer_in_).md>) — Composes the composited video frame with a Core Animation layer. _(deprecated)_
- [+ videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:](<init(postprocessingasvideolayers_in_).md>) — Composes the composited video frames with the Core Animation layer.
- [init(configuration:)](<init(configuration_).md>) — Compose the composited video frames with the Core Animation layer.
