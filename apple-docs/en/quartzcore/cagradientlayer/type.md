---
title: type
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cagradientlayer/type
source_url: 'https://developer.apple.com/documentation/quartzcore/cagradientlayer/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cagradientlayer/type.json'
content_hash: 'sha256:4e353b7b6f49563e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAGradientLayer](../cagradientlayer.md)

# type

<sub>Instance Property</sub>

Style of gradient drawn by the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var type: CAGradientLayerType { get set }
```

## Discussion

Defaults to [kCAGradientLayerAxial](../cagradientlayertype/axial.md).

## See Also

### Gradient Style Properties

- [colors](colors.md) — An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [locations](locations.md) — An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [endPoint](endpoint.md) — The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [startPoint](startpoint.md) — The start point of the gradient when drawn in the layer’s coordinate space. Animatable.
