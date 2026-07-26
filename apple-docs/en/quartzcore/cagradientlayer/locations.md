---
title: locations
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cagradientlayer/locations
source_url: 'https://developer.apple.com/documentation/quartzcore/cagradientlayer/locations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cagradientlayer/locations.json'
content_hash: 'sha256:3e3ee8fdabdf09f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAGradientLayer](../cagradientlayer.md)

# locations

<sub>Instance Property</sub>

An optional array of NSNumber objects defining the location of each gradient stop. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var locations: [NSNumber]? { get set }
```

## Discussion

The gradient stops are specified as values between `0` and `1`. The values must be monotonically increasing. If `nil`, the stops are spread uniformly across the range. Defaults to `nil`.

When rendered, the colors are mapped to the output color space before being interpolated.

## See Also

### Gradient Style Properties

- [colors](colors.md) — An array of `CGColorRef` objects defining the color of each gradient stop. Animatable.
- [endPoint](endpoint.md) — The end point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [startPoint](startpoint.md) — The start point of the gradient when drawn in the layer’s coordinate space. Animatable.
- [type](type.md) — Style of gradient drawn by the layer.
