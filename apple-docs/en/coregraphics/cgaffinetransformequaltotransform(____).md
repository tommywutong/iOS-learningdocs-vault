---
title: 'CGAffineTransformEqualToTransform(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransformequaltotransform(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransformequaltotransform(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransformequaltotransform%28_%3A_%3A%29.json'
content_hash: 'sha256:d618a6243c066637'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformEqualToTransform(_:_:)

<sub>Function</sub>

Checks whether two affine transforms are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformEqualToTransform(_ t1: CGAffineTransform, _ t2: CGAffineTransform) -> Bool
```

## Parameters

- `t1` — An affine transform.

- `t2` — An affine transform.

## Return Value

Returns `true` if `t1` and `t2` are equal, `false` otherwise.

## See Also

### Evaluating Affine Transforms

- [CGAffineTransformIsIdentity](<cgaffinetransformisidentity(__).md>) — Checks whether an affine transform is the identity transform.
