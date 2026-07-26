---
title: 'setCenter(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/setcenter(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/setcenter(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/setcenter%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:b8f2817f2434bfd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# setCenter(_:animated:)

<sub>Instance Method</sub>

Changes the center coordinate of the map, and optionally animates the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCenter(_ coordinate: CLLocationCoordinate2D, animated: Bool)
```

## Parameters

- `coordinate` — The new center coordinate for the map.

- `animated` — Specify [true](../../swift/true.md) if you want the map view to scroll to the new location or [false](../../swift/false.md) if you want the map to display the new location immediately.

## Discussion

Changing the center coordinate centers the map on the new coordinate without changing the current zoom level. It also updates the value in the [region](region.md) property to reflect the new center coordinate and the new span values needed to maintain the current zoom level.

## See Also

### Manipulating the visible portion of the map

- [region](region.md) — The area the map view displays.
- [- setRegion:animated:](<setregion(__animated_).md>) — Changes the currently visible region, and optionally animates the change.
- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [- showAnnotations:animated:](<showannotations(__animated_).md>) — Sets the visible region so that the map displays the specified annotations.
- [visibleMapRect](visiblemaprect.md) — The area visible in the map view.
- [- setVisibleMapRect:animated:](<setvisiblemaprect(__animated_).md>) — Changes the currently visible portion of the map, and optionally animates the change.
- [- setVisibleMapRect:edgePadding:animated:](<setvisiblemaprect(__edgepadding_animated_).md>) — Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
