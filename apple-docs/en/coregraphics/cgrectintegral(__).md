---
title: 'CGRectIntegral(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectintegral(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectintegral(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectintegral%28_%3A%29.json'
content_hash: 'sha256:e7eba0000897b37d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectIntegral(_:)

<sub>Function</sub>

Returns the smallest rectangle that results from converting the source rectangle values to integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectIntegral(_ rect: CGRect) -> CGRect
```

## Parameters

- `rect` — The source rectangle.

## Return Value

A rectangle with the smallest integer values for its origin and size that contains the source rectangle. That is, given a rectangle with fractional origin or size values, `CGRectIntegral` rounds the rectangle’s origin downward and its size upward to the nearest whole integers, such that the result contains the original rectangle. Returns a null rectangle if `rect` is a null rectangle.

## See Also

### Modifying Rectangles

- [CGRectInset](<cgrectinset(______).md>) — Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [CGRectIntersection](<cgrectintersection(____).md>) — Returns the intersection of two rectangles.
- [CGRectOffset](<cgrectoffset(______).md>) — Returns a rectangle with an origin that is offset from that of the source rectangle.
- [CGRectStandardize](<cgrectstandardize(__).md>) — Returns a rectangle with a positive width and height.
- [CGRectUnion](<cgrectunion(____).md>) — Returns the smallest rectangle that contains the two source rectangles.
