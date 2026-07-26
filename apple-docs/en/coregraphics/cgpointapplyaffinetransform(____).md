---
title: 'CGPointApplyAffineTransform(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpointapplyaffinetransform(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpointapplyaffinetransform(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpointapplyaffinetransform%28_%3A_%3A%29.json'
content_hash: 'sha256:577c770613b67213'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPointApplyAffineTransform(_:_:)

<sub>Function</sub>

Returns the point resulting from an affine transformation of an existing point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPointApplyAffineTransform(_ point: CGPoint, _ t: CGAffineTransform) -> CGPoint
```

## Parameters

- `point` — A point that specifies the x- and y-coordinates to transform.

- `t` — The affine transform to apply.

## Return Value

A new point resulting from applying the specified affine transform to the existing point.

## See Also

### Applying Affine Transformations

- [CGSizeApplyAffineTransform](<cgsizeapplyaffinetransform(____).md>) — Returns the height and width resulting from a transformation of an existing height and width.
- [CGRectApplyAffineTransform](<cgrectapplyaffinetransform(____).md>) — Applies an affine transform to a rectangle.
