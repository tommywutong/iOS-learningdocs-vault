---
title: 'MKMapRectDivide(_:_:_:_:_:)'
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprectdivide(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprectdivide(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprectdivide%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d8ef03949579384e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapRectDivide(_:_:_:_:_:)

<sub>Function</sub>

Divides the specified rectangle into two smaller rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func MKMapRectDivide(_ rect: MKMapRect, _ slice: UnsafeMutablePointer<MKMapRect>, _ remainder: UnsafeMutablePointer<MKMapRect>, _ amount: Double, _ edge: CGRectEdge)
```

## Parameters

- `rect` — The rectangle to divide.

- `slice` — On input, a pointer to a map rectangle. On output, this parameter contains the portion of `rect` that the method removes.

- `remainder` — On input, a pointer to a map rectangle. On output, this parameter contains the remaining portion of `rect` that the method doesn’t remove.

- `amount` — The amount of `rect` to remove along the specified edge. If this value is negative, the system sets it to `0`.

- `edge` — The edge from which to remove the specified amount.

## See Also

### Modifying the rectangle

- [MKMapRectUnion](<mkmaprect/union(__).md>) — Returns a rectangle that represents the union of two rectangles.
- [MKMapRectIntersection](<mkmaprect/intersection(__).md>) — Returns the rectangle that represents the intersection of two rectangles.
- [MKMapRectInset](<mkmaprect/insetby(dx_dy_).md>) — Returns the specified rectangle with an inset by the specified amounts.
- [MKMapRectOffset](<mkmaprect/offsetby(dx_dy_).md>) — Returns a rectangle with an origin point that shifts by the specified amount.
