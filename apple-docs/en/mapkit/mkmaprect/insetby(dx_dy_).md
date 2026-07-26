---
title: 'insetBy(dx:dy:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/insetby(dx:dy:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/insetby(dx:dy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/insetby%28dx%3Ady%3A%29.json'
content_hash: 'sha256:f22e639dcd328664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# insetBy(dx:dy:)

<sub>Instance Method</sub>

Returns the specified rectangle with an inset by the specified amounts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insetBy(dx: Double, dy: Double) -> MKMapRect
```

## Parameters

- `dx` — The amount (in map points) to subtract from both sides along the x-axis.

- `dy` — The amount (in map points) to subtract from both sides along the x-axis.

## Return Value

The inset rectangle. If the original rectangle was null, that rectangle is returned instead.

## See Also

### Modifying the rectangle

- [MKMapRectUnion](<union(__).md>) — Returns a rectangle that represents the union of two rectangles.
- [MKMapRectIntersection](<intersection(__).md>) — Returns the rectangle that represents the intersection of two rectangles.
- [MKMapRectOffset](<offsetby(dx_dy_).md>) — Returns a rectangle with an origin point that shifts by the specified amount.
- [MKMapRectDivide](<../mkmaprectdivide(__________).md>) — Divides the specified rectangle into two smaller rectangles.
