---
title: 'intersection(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/intersection(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/intersection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/intersection%28_%3A%29.json'
content_hash: 'sha256:1d645daa146ce999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# intersection(_:)

<sub>Instance Method</sub>

Returns the rectangle that represents the intersection of two rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersection(_ rect2: MKMapRect) -> MKMapRect
```

## Parameters

- `rect2` — The second rectangle.

## Return Value

The rectangle representing the intersection of the two rectangles, or [MKMapRectNull](null.md) if there’s no intersection.

## See Also

### Modifying the rectangle

- [MKMapRectUnion](<union(__).md>) — Returns a rectangle that represents the union of two rectangles.
- [MKMapRectInset](<insetby(dx_dy_).md>) — Returns the specified rectangle with an inset by the specified amounts.
- [MKMapRectOffset](<offsetby(dx_dy_).md>) — Returns a rectangle with an origin point that shifts by the specified amount.
- [MKMapRectDivide](<../mkmaprectdivide(__________).md>) — Divides the specified rectangle into two smaller rectangles.
