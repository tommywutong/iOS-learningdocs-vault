---
title: 'CGSizeApplyAffineTransform(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgsizeapplyaffinetransform(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsizeapplyaffinetransform(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsizeapplyaffinetransform%28_%3A_%3A%29.json'
content_hash: 'sha256:2e02b87a0dda0079'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSizeApplyAffineTransform(_:_:)

<sub>Function</sub>

Returns the height and width resulting from a transformation of an existing height and width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGSizeApplyAffineTransform(_ size: CGSize, _ t: CGAffineTransform) -> CGSize
```

## Parameters

- `size` — A size that specifies the height and width to transform.

- `t` — The affine transform to apply.

## Return Value

A new size resulting from applying the specified affine transform to the existing size.

## See Also

### Applying Affine Transformations

- [CGPointApplyAffineTransform](<cgpointapplyaffinetransform(____).md>) — Returns the point resulting from an affine transformation of an existing point.
- [CGRectApplyAffineTransform](<cgrectapplyaffinetransform(____).md>) — Applies an affine transform to a rectangle.
