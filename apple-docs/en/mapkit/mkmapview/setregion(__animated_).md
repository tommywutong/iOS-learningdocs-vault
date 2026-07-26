---
title: 'setRegion(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/setregion(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/setregion(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/setregion%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:76913e2dfced0545'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# setRegion(_:animated:)

<sub>Instance Method</sub>

Changes the currently visible region, and optionally animates the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setRegion(_ region: MKCoordinateRegion, animated: Bool)
```

## Parameters

- `region` — The new region to display in the map view.

- `animated` — Specify [true](../../swift/true.md) if you want the map view to animate the transition to the new region, or [false](../../swift/false.md) if you want the map to center on the specified region immediately.

## Discussion

Changing just the center coordinate of the region can still cause the span values to change implicitly. The span values might change because the distances that a span repesents change at different latitudes and longitudes, and the map view may need to adjust the span to account for the new location. If you want to change the center coordinate without changing the zoom level, use the [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) instead.

When setting a new region, the map may adjust the value in the `region` parameter so that it fits the visible area of the map precisely. This adjustment ensures that the value in the [region](region.md) property reflects the visible portion of the map. However, it does mean that if you get the value of that property right after calling this method, the returned value may not match the value you set. You can use the [- regionThatFits:](<regionthatfits(__).md>) method to determine the region that the map sets.

## See Also

### Manipulating the visible portion of the map

- [region](region.md) — The area the map view displays.
- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) — Changes the center coordinate of the map, and optionally animates the change.
- [- showAnnotations:animated:](<showannotations(__animated_).md>) — Sets the visible region so that the map displays the specified annotations.
- [visibleMapRect](visiblemaprect.md) — The area visible in the map view.
- [- setVisibleMapRect:animated:](<setvisiblemaprect(__animated_).md>) — Changes the currently visible portion of the map, and optionally animates the change.
- [- setVisibleMapRect:edgePadding:animated:](<setvisiblemaprect(__edgepadding_animated_).md>) — Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
