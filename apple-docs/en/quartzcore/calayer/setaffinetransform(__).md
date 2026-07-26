---
title: 'setAffineTransform(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/setaffinetransform(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/setaffinetransform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/setaffinetransform%28_%3A%29.json'
content_hash: 'sha256:fec2059aa0b45480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# setAffineTransform(_:)

<sub>Instance Method</sub>

Sets the layer’s transform to the specified affine transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setAffineTransform(_ m: CGAffineTransform)
```

## Parameters

- `m` — The affine transform to use for the layer’s transform.

## See Also

### Managing the layer’s transform

- [transform](transform.md) — The transform applied to the layer’s contents. Animatable.
- [sublayerTransform](sublayertransform.md) — Specifies the transform to apply to sublayers when rendering. Animatable.
- [- affineTransform](<affinetransform().md>) — Returns an affine version of the layer’s transform.
