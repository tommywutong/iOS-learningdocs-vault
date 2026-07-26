---
title: 'offsetBy(dx:dy:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/offsetby(dx:dy:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/offsetby(dx:dy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/offsetby%28dx%3Ady%3A%29.json'
content_hash: 'sha256:0f5d246124743fd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# offsetBy(dx:dy:)

<sub>Instance Method</sub>

Returns a rectangle with an origin point that shifts by the specified amount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func offsetBy(dx: Double, dy: Double) -> MKMapRect
```

## Parameters

- `dx` — The amount (in map points) to shift the x-coordinate of the origin point.

- `dy` — The amount (in map points) to shift the x-coordinate of the origin point.

## Return Value

The offset rectangle. If the original rectangle is `null`, that rectangle returns instead.

## See Also

### Modifying the rectangle

- [MKMapRectUnion](<union(__).md>) — Returns a rectangle that represents the union of two rectangles.
- [MKMapRectIntersection](<intersection(__).md>) — Returns the rectangle that represents the intersection of two rectangles.
- [MKMapRectInset](<insetby(dx_dy_).md>) — Returns the specified rectangle with an inset by the specified amounts.
- [MKMapRectDivide](<../mkmaprectdivide(__________).md>) — Divides the specified rectangle into two smaller rectangles.
