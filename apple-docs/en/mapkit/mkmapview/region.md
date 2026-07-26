---
title: region
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/region
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/region.json'
content_hash: 'sha256:851523d196ec9654'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# region

<sub>Instance Property</sub>

The area the map view displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var region: MKCoordinateRegion { get set }
```

## Discussion

The _region_ encompasses both the latitude and longitude center point of the map, and the span of coordinates to display. The span values provide an implicit zoom value for the map. The larger the displayed area, the lower the amount of zoom. Similarly, the smaller the displayed area, the greater the amount of zoom.

Changing only the center coordinate of the region can still cause the span to change implicitly. The span might change because the distances that a span represents change at different latitudes and longitudes, and the map view may need to adjust the span to account for the new location. If you want to change the center coordinate without changing the zoom level, use the [centerCoordinate](centercoordinate.md) instead.

Changing the value of this property updates the map view immediately. When setting this property, the map may adjust the new region value so that it fits the visible area of the map precisely. This ensures that the value in this property reflects the visible portion of the map. However, it does mean that if you get the value of this property right after setting it, the returned value may not match the value you set. You can use the [- regionThatFits:](<regionthatfits(__).md>) method to determine the region that the map sets.

If you want to animate the change in region, use the [- setRegion:animated:](<setregion(__animated_).md>) method instead.

## See Also

### Manipulating the visible portion of the map

- [- setRegion:animated:](<setregion(__animated_).md>) — Changes the currently visible region, and optionally animates the change.
- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) — Changes the center coordinate of the map, and optionally animates the change.
- [- showAnnotations:animated:](<showannotations(__animated_).md>) — Sets the visible region so that the map displays the specified annotations.
- [visibleMapRect](visiblemaprect.md) — The area visible in the map view.
- [- setVisibleMapRect:animated:](<setvisiblemaprect(__animated_).md>) — Changes the currently visible portion of the map, and optionally animates the change.
- [- setVisibleMapRect:edgePadding:animated:](<setvisiblemaprect(__edgepadding_animated_).md>) — Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
