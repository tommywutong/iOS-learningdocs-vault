---
title: sublayerTransform
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/sublayertransform
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/sublayertransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/sublayertransform.json'
content_hash: 'sha256:9e981eb247d7f909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# sublayerTransform

<sub>Instance Property</sub>

Specifies the transform to apply to sublayers when rendering. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sublayerTransform: CATransform3D { get set }
```

## Discussion

You typically use this property to add perspective and other viewing effects to embedded layers. You add perspective by setting the sublayer transform to the desired projection matrix. The default value of this property is the identity transform.

## See Also

### Managing the layer’s transform

- [transform](transform.md) — The transform applied to the layer’s contents. Animatable.
- [- affineTransform](<affinetransform().md>) — Returns an affine version of the layer’s transform.
- [- setAffineTransform:](<setaffinetransform(__).md>) — Sets the layer’s transform to the specified affine transform.
