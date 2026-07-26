---
title: affineTransform()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/affinetransform()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/affinetransform()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/affinetransform%28%29.json'
content_hash: 'sha256:33a14801c5c35d15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# affineTransform()

<sub>Instance Method</sub>

Returns an affine version of the layer’s transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func affineTransform() -> CGAffineTransform
```

## Return Value

The affine transform structure that corresponds to the value in the layer’s [transform](transform.md) property.

## See Also

### Managing the layer’s transform

- [transform](transform.md) — The transform applied to the layer’s contents. Animatable.
- [sublayerTransform](sublayertransform.md) — Specifies the transform to apply to sublayers when rendering. Animatable.
- [- setAffineTransform:](<setaffinetransform(__).md>) — Sets the layer’s transform to the specified affine transform.
