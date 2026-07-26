---
title: 'setVisibleMapRect(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/setvisiblemaprect(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/setvisiblemaprect(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/setvisiblemaprect%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:a632b34cd78b70ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# setVisibleMapRect(_:animated:)

<sub>Instance Method</sub>

Changes the currently visible portion of the map, and optionally animates the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setVisibleMapRect(_ mapRect: MKMapRect, animated animate: Bool)
```

## Parameters

- `mapRect` — The map rectangle to make visible in the map view.

- `animate` — Specify [true](../../swift/true.md) if you want the map view to animate the transition to the new map rectangle or [false](../../swift/false.md) if you want the map to center on the specified rectangle immediately.

## See Also

### Manipulating the visible portion of the map

- [region](region.md) — The area the map view displays.
- [- setRegion:animated:](<setregion(__animated_).md>) — Changes the currently visible region, and optionally animates the change.
- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) — Changes the center coordinate of the map, and optionally animates the change.
- [- showAnnotations:animated:](<showannotations(__animated_).md>) — Sets the visible region so that the map displays the specified annotations.
- [visibleMapRect](visiblemaprect.md) — The area visible in the map view.
- [- setVisibleMapRect:edgePadding:animated:](<setvisiblemaprect(__edgepadding_animated_).md>) — Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
