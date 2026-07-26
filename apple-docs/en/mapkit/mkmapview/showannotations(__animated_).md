---
title: 'showAnnotations(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/showannotations(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/showannotations(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/showannotations%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:d17d6962d88f642d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# showAnnotations(_:animated:)

<sub>Instance Method</sub>

Sets the visible region so that the map displays the specified annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func showAnnotations(_ annotations: [any MKAnnotation], animated: Bool)
```

## Parameters

- `annotations` — The annotations that you want to be visible on the map.

- `animated` — Specify [true](../../swift/true.md) if you want the map view to animate the region change, or [false](../../swift/false.md) if you want the map to display the new region immediately without animations.

## Discussion

Calling this method updates the value in the [region](region.md) property, and potentially other properties, to reflect the new map region.

## See Also

### Manipulating the visible portion of the map

- [region](region.md) — The area the map view displays.
- [- setRegion:animated:](<setregion(__animated_).md>) — Changes the currently visible region, and optionally animates the change.
- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) — Changes the center coordinate of the map, and optionally animates the change.
- [visibleMapRect](visiblemaprect.md) — The area visible in the map view.
- [- setVisibleMapRect:animated:](<setvisiblemaprect(__animated_).md>) — Changes the currently visible portion of the map, and optionally animates the change.
- [- setVisibleMapRect:edgePadding:animated:](<setvisiblemaprect(__edgepadding_animated_).md>) — Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
