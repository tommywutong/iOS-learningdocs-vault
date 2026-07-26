---
title: 'CGRectStandardize(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectstandardize(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectstandardize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectstandardize%28_%3A%29.json'
content_hash: 'sha256:2f9eb6aadb4d76e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectStandardize(_:)

<sub>Function</sub>

Returns a rectangle with a positive width and height.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectStandardize(_ rect: CGRect) -> CGRect
```

## Parameters

- `rect` — The source rectangle.

## Return Value

A rectangle that represents the source rectangle, but with positive width and height values. Returns a null rectangle if `rect` is a null rectangle.

## See Also

### Modifying Rectangles

- [CGRectInset](<cgrectinset(______).md>) — Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [CGRectIntegral](<cgrectintegral(__).md>) — Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [CGRectIntersection](<cgrectintersection(____).md>) — Returns the intersection of two rectangles.
- [CGRectOffset](<cgrectoffset(______).md>) — Returns a rectangle with an origin that is offset from that of the source rectangle.
- [CGRectUnion](<cgrectunion(____).md>) — Returns the smallest rectangle that contains the two source rectangles.
