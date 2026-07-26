---
title: 'CGRectIntersection(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectintersection(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectintersection(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectintersection%28_%3A_%3A%29.json'
content_hash: 'sha256:73b12eeca38aa221'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectIntersection(_:_:)

<sub>Function</sub>

Returns the intersection of two rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectIntersection(_ r1: CGRect, _ r2: CGRect) -> CGRect
```

## Parameters

- `r1` — The first source rectangle.

- `r2` — The second source rectangle.

## Return Value

A rectangle that represents the intersection of the two specified rectangles. If the two rectangles do not intersect, returns the null rectangle. To check for this condition, use [CGRectIsNull](<cgrectisnull(__).md>).

## Discussion

Both rectangles are standardized prior to calculating the intersection.

## See Also

### Modifying Rectangles

- [CGRectInset](<cgrectinset(______).md>) — Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [CGRectIntegral](<cgrectintegral(__).md>) — Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [CGRectOffset](<cgrectoffset(______).md>) — Returns a rectangle with an origin that is offset from that of the source rectangle.
- [CGRectStandardize](<cgrectstandardize(__).md>) — Returns a rectangle with a positive width and height.
- [CGRectUnion](<cgrectunion(____).md>) — Returns the smallest rectangle that contains the two source rectangles.
