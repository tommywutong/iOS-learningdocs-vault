---
title: 'CGRectUnion(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectunion(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectunion(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectunion%28_%3A_%3A%29.json'
content_hash: 'sha256:ef5385ab291de2a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectUnion(_:_:)

<sub>Function</sub>

Returns the smallest rectangle that contains the two source rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectUnion(_ r1: CGRect, _ r2: CGRect) -> CGRect
```

## Parameters

- `r1` — The first source rectangle.

- `r2` — The second source rectangle.

## Return Value

The smallest rectangle that completely contains both of the source rectangles.

## Discussion

Both rectangles are standardized prior to calculating the union. If either of the rectangles is a null rectangle, a copy of the other rectangle is returned (resulting in a null rectangle if both rectangles are null). Otherwise a rectangle that completely contains the source rectangles is returned.

## See Also

### Modifying Rectangles

- [CGRectInset](<cgrectinset(______).md>) — Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [CGRectIntegral](<cgrectintegral(__).md>) — Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [CGRectIntersection](<cgrectintersection(____).md>) — Returns the intersection of two rectangles.
- [CGRectOffset](<cgrectoffset(______).md>) — Returns a rectangle with an origin that is offset from that of the source rectangle.
- [CGRectStandardize](<cgrectstandardize(__).md>) — Returns a rectangle with a positive width and height.
