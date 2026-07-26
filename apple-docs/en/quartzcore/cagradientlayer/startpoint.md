---
title: startPoint
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cagradientlayer/startpoint
source_url: 'https://developer.apple.com/documentation/quartzcore/cagradientlayer/startpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cagradientlayer/startpoint.json'
content_hash: 'sha256:6ee3155e6e313d16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAGradientLayer](../cagradientlayer.md)

# startPoint

<sub>Instance Property</sub>

The start point of the gradient when drawn in the layer’s coordinate space. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var startPoint: CGPoint { get set }
```

## Discussion

The start point corresponds to the first stop of the gradient. The point is defined in the unit coordinate space and is then mapped to the layer’s bounds rectangle when drawn.

Default value is `(0.5,0.0)`.

## See Also

### Gradient Style Properties

- [colors](colors.md) — An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [locations](locations.md) — An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [endPoint](endpoint.md) — The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [type](type.md) — Style of gradient drawn by the layer.
