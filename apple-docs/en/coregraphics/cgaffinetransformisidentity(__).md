---
title: 'CGAffineTransformIsIdentity(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgaffinetransformisidentity(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgaffinetransformisidentity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgaffinetransformisidentity%28_%3A%29.json'
content_hash: 'sha256:c89b6b4f4ab7794b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAffineTransformIsIdentity(_:)

<sub>Function</sub>

Checks whether an affine transform is the identity transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGAffineTransformIsIdentity(_ t: CGAffineTransform) -> Bool
```

## Parameters

- `t` — The affine transform to check.

## Return Value

Returns `true` if `t` is the identity transform, `false` otherwise.

## See Also

### Evaluating Affine Transforms

- [CGAffineTransformEqualToTransform](<cgaffinetransformequaltotransform(____).md>) — Checks whether two affine transforms are equal.
