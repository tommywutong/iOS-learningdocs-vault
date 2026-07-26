---
title: layers
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/layers
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/layers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/layers.json'
content_hash: 'sha256:dad353cfbf9f239c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionCoreAnimationTool](../../avvideocompositioncoreanimationtool.md) · [Configuration](../configuration.md)

# layers

<sub>Instance Property</sub>

Layer(s) to contain the composited video frames. Frames are duplicated if there is more than one layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layers: [CALayer]
```

## See Also

### Inspecting the configuration

- [containingLayer](containinglayer.md) — Containing layer to be rendered into, producing the final frame.
