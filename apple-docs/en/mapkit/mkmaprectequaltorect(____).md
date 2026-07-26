---
title: 'MKMapRectEqualToRect(_:_:)'
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprectequaltorect(_:_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprectequaltorect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprectequaltorect%28_%3A_%3A%29.json'
content_hash: 'sha256:94b9ed6fc81de2d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapRectEqualToRect(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether two map rectangles are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func MKMapRectEqualToRect(_ rect1: MKMapRect, _ rect2: MKMapRect) -> Bool
```

## Parameters

- `rect1` — The first map rectangle.

- `rect2` — The second map rectangle.

## Return Value

[true](../swift/true.md) if the rectangles are exactly the same, or [false](../swift/false.md) if the origin point or size values are different.

## See Also

### Comparing rectangles

- [MKMapRectIsNull](mkmaprect/isnull.md) — A Boolean value that indicates whether the specified rectangle is null.
- [MKMapRectIsEmpty](mkmaprect/isempty.md) — A Boolean value that indicates whether the specified rectangle has no area.
- [MKMapRectSpans180thMeridian](mkmaprect/spans180thmeridian.md) — A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
- [MKMapRectRemainder](mkmaprect/remainder.md) — A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.
