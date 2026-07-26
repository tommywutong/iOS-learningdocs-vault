---
title: 'init(postProcessingAsVideoLayers:containingLayer:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/init(postprocessingasvideolayers:containinglayer:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/init(postprocessingasvideolayers:containinglayer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/init%28postprocessingasvideolayers%3Acontaininglayer%3A%29.json'
content_hash: 'sha256:f4fbfc81cbce3909'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionCoreAnimationTool](../../avvideocompositioncoreanimationtool.md) · [Configuration](../configuration.md)

# init(postProcessingAsVideoLayers:containingLayer:)

<sub>Initializer</sub>

Duplicate the composited video frames in each videoLayer and render animationLayer to produce the final frame. Normally videoLayers should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(postProcessingAsVideoLayers layers: [CALayer], containingLayer: CALayer)
```

## See Also

### Creating a configuration

- [init(postProcessingAsVideoLayer:containingLayer:)](<init(postprocessingasvideolayer_containinglayer_).md>) — Place composited video frames in videoLayer and render animationLayer to produce the final frame. Normally videoLayer should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.
