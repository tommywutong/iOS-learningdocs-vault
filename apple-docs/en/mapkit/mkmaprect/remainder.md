---
title: remainder
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmaprect/remainder
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/remainder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/remainder.json'
content_hash: 'sha256:a16c82f6e6290618'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# remainder

<sub>Instance Property</sub>

A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var remainder: MKMapRect { get }
```

## Discussion

For a rectangle that lies on the 180th meridian, this function isolates the portion that lies outside the boundary, wraps it to the opposite side of the map, and returns that rectangle.

## See Also

### Comparing rectangles

- [MKMapRectIsNull](isnull.md) — A Boolean value that indicates whether the specified rectangle is null.
- [MKMapRectEqualToRect](<../mkmaprectequaltorect(____).md>) — Returns a Boolean value that indicates whether two map rectangles are equal.
- [MKMapRectIsEmpty](isempty.md) — A Boolean value that indicates whether the specified rectangle has no area.
- [MKMapRectSpans180thMeridian](spans180thmeridian.md) — A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
