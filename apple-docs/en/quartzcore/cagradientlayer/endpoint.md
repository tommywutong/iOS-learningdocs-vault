---
title: endPoint
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cagradientlayer/endpoint
source_url: 'https://developer.apple.com/documentation/quartzcore/cagradientlayer/endpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cagradientlayer/endpoint.json'
content_hash: 'sha256:c23b76b04ec115c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAGradientLayer](../cagradientlayer.md)

# endPoint

<sub>Instance Property</sub>

The end point of the gradient when drawn in the layer’s coordinate space. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var endPoint: CGPoint { get set }
```

## Discussion

The end point corresponds to the last stop of the gradient. The point is defined in the unit coordinate space and is then mapped to the layer’s bounds rectangle when drawn.

Default value is `(0.5,1.0)`.

## See Also

### Gradient Style Properties

- [colors](colors.md) — An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [locations](locations.md) — An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [startPoint](startpoint.md) — The start point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [type](type.md) — Style of gradient drawn by the layer.
