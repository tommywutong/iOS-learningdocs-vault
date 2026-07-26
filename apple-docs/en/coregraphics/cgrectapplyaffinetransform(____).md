---
title: 'CGRectApplyAffineTransform(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectapplyaffinetransform(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectapplyaffinetransform(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectapplyaffinetransform%28_%3A_%3A%29.json'
content_hash: 'sha256:a5d229de4871d64c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectApplyAffineTransform(_:_:)

<sub>Function</sub>

Applies an affine transform to a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectApplyAffineTransform(_ rect: CGRect, _ t: CGAffineTransform) -> CGRect
```

## Parameters

- `rect` — The rectangle whose corner points you want to transform.

- `t` — The affine transform to apply to the `rect` parameter.

## Return Value

The transformed rectangle.

## Discussion

Because affine transforms do not preserve rectangles in general, this function returns the smallest rectangle that contains the transformed corner points of the `rect` parameter. If the affine transform `t` consists solely of scaling and translation operations, then the returned rectangle coincides with the rectangle constructed from the four transformed corners.

## See Also

### Applying Affine Transformations

- [CGPointApplyAffineTransform](<cgpointapplyaffinetransform(____).md>) — Returns the point resulting from an affine transformation of an existing point.
- [CGSizeApplyAffineTransform](<cgsizeapplyaffinetransform(____).md>) — Returns the height and width resulting from a transformation of an existing height and width.
