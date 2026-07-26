---
title: centerCoordinate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/centercoordinate
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/centercoordinate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/centercoordinate.json'
content_hash: 'sha256:972e7d3ef7dcd1bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# centerCoordinate

<sub>Instance Property</sub>

The map coordinate at the center of the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var centerCoordinate: CLLocationCoordinate2D { get set }
```

## Discussion

Changing the value in this property centers the map on the new coordinate without changing the current zoom level. It also updates the values in the [region](region.md) property to reflect the new center coordinate and the new span values needed to maintain the current zoom level.

Changing the value of this property updates the map view immediately. If you want to animate the change, use the [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) method instead.

## See Also

### Manipulating the visible portion of the map

- [region](region.md) — The area the map view displays.
- [- setRegion:animated:](<setregion(__animated_).md>) — Changes the currently visible region, and optionally animates the change.
- [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) — Changes the center coordinate of the map, and optionally animates the change.
- [- showAnnotations:animated:](<showannotations(__animated_).md>) — Sets the visible region so that the map displays the specified annotations.
- [visibleMapRect](visiblemaprect.md) — The area visible in the map view.
- [- setVisibleMapRect:animated:](<setvisiblemaprect(__animated_).md>) — Changes the currently visible portion of the map, and optionally animates the change.
- [- setVisibleMapRect:edgePadding:animated:](<setvisiblemaprect(__edgepadding_animated_).md>) — Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
