---
title: isNull
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmaprect/isnull
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/isnull'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/isnull.json'
content_hash: 'sha256:74d6d84005d2e7f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# isNull

<sub>Instance Property</sub>

A Boolean value that indicates whether the specified rectangle is null.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isNull: Bool { get }
```

## Discussion

For this class, a rectangle is `null` if its origin point contains an invalid or infinite value.

## See Also

### Comparing rectangles

- [MKMapRectEqualToRect](<../mkmaprectequaltorect(____).md>) — Returns a Boolean value that indicates whether two map rectangles are equal.
- [MKMapRectIsEmpty](isempty.md) — A Boolean value that indicates whether the specified rectangle has no area.
- [MKMapRectSpans180thMeridian](spans180thmeridian.md) — A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
- [MKMapRectRemainder](remainder.md) — A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.
