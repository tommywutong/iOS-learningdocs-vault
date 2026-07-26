---
title: path
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayer/path
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayer/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayer/path.json'
content_hash: 'sha256:b7634cb608d082a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayer](../cashapelayer.md)

# path

<sub>Instance Property</sub>

The path defining the shape to be rendered. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var path: CGPath? { get set }
```

## Discussion

Unlike most animatable properties, [path](path.md) (as with all [CGPath](../../coregraphics/cgpath.md) animatable properties) does not support implicit animation.

The path object may be animated using any of the concrete subclasses of [CAPropertyAnimation](../capropertyanimation.md). Paths will interpolate as a linear blend of  the “on-line” points; “off-line” points may be interpolated non-linearly (e.g. to preserve continuity of the curve’s derivative). If the two paths have a different number of control points or segments the results are undefined. If the path extends outside the layer bounds it will not automatically be clipped to the layer, only if the normal layer masking rules cause that.

The default value of this property is `nil`.
