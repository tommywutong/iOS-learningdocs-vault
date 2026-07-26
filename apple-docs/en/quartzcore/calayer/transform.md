---
title: transform
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/transform
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/transform.json'
content_hash: 'sha256:e2acc3c7d46b7c6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# transform

<sub>Instance Property</sub>

The transform applied to the layer’s contents. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var transform: CATransform3D { get set }
```

## Discussion

This property is set to the identity transform by default. Any transformations you apply to the layer occur relative to the layer’s anchor point.

## See Also

### Managing the layer’s transform

- [sublayerTransform](sublayertransform.md) — Specifies the transform to apply to sublayers when rendering. Animatable.
- [- affineTransform](<affinetransform().md>) — Returns an affine version of the layer’s transform.
- [- setAffineTransform:](<setaffinetransform(__).md>) — Sets the layer’s transform to the specified affine transform.
