---
title: 'CGRectInset(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectinset(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectinset(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectinset%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f260f954c6dee2d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectInset(_:_:_:)

<sub>Function</sub>

Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectInset(_ rect: CGRect, _ dx: CGFloat, _ dy: CGFloat) -> CGRect
```

## Parameters

- `rect` — The source [CGRect](../corefoundation/cgrect.md) structure.

- `dx` — The x-coordinate value to use for adjusting the source rectangle. To create an inset rectangle, specify a positive value. To create a larger, encompassing rectangle, specify a negative value.

- `dy` — The y-coordinate value to use for adjusting the source rectangle. To create an inset rectangle, specify a positive value. To create a larger, encompassing rectangle, specify a negative value.

## Return Value

A rectangle. The origin value is offset in the x-axis by the distance specified by the `dx` parameter and in the y-axis by the distance specified by the `dy` parameter, and its size adjusted by `(2*dx,2*dy)`, relative to the source rectangle. If `dx` and `dy` are positive values, then the rectangle’s size is decreased. If `dx` and `dy` are negative values, the rectangle’s size is increased.

## Discussion

The rectangle is standardized and then the inset parameters are applied. If the resulting rectangle would have a negative height or width, a null rectangle is returned.

## See Also

### Modifying Rectangles

- [CGRectIntegral](<cgrectintegral(__).md>) — Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [CGRectIntersection](<cgrectintersection(____).md>) — Returns the intersection of two rectangles.
- [CGRectOffset](<cgrectoffset(______).md>) — Returns a rectangle with an origin that is offset from that of the source rectangle.
- [CGRectStandardize](<cgrectstandardize(__).md>) — Returns a rectangle with a positive width and height.
- [CGRectUnion](<cgrectunion(____).md>) — Returns the smallest rectangle that contains the two source rectangles.
