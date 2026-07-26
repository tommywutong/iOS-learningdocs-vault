---
title: 'union(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/union(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/union(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/union%28_%3A%29.json'
content_hash: 'sha256:224b5d717ea77af1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# union(_:)

<sub>Instance Method</sub>

Returns a rectangle that represents the union of two rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func union(_ rect2: MKMapRect) -> MKMapRect
```

## Parameters

- `rect2` — The second rectangle.

## Return Value

A rectangle with an area that encompasses the two rectangles and the space between them.

## Discussion

If either rectangle is `null`, this method returns the other rectangle. This method sets the origin point of the returned rectangle to the smaller of the x and y values for the two rectangles. Similarly, the method computes the size and width of the rectangle by taking the maximum x and y values and subtracting the x and y values for the new origin point.

## See Also

### Modifying the rectangle

- [MKMapRectIntersection](<intersection(__).md>) — Returns the rectangle that represents the intersection of two rectangles.
- [MKMapRectInset](<insetby(dx_dy_).md>) — Returns the specified rectangle with an inset by the specified amounts.
- [MKMapRectOffset](<offsetby(dx_dy_).md>) — Returns a rectangle with an origin point that shifts by the specified amount.
- [MKMapRectDivide](<../mkmaprectdivide(__________).md>) — Divides the specified rectangle into two smaller rectangles.
