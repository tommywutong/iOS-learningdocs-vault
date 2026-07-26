---
title: colors
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cagradientlayer/colors
source_url: 'https://developer.apple.com/documentation/quartzcore/cagradientlayer/colors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cagradientlayer/colors.json'
content_hash: 'sha256:e551834c63fa20a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAGradientLayer](../cagradientlayer.md)

# colors

<sub>Instance Property</sub>

An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colors: [Any]? { get set }
```

## Discussion

Defaults to `nil`.

## See Also

### Gradient Style Properties

- [locations](locations.md) — An optional array of NSNumber objects defining the location of each gradient stop. Animatable.
- [endPoint](endpoint.md) — The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [startPoint](startpoint.md) — The start point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [type](type.md) — Style of gradient drawn by the layer.
