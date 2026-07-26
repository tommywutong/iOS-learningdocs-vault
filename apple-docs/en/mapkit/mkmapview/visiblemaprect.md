---
title: visibleMapRect
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/visiblemaprect
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/visiblemaprect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/visiblemaprect.json'
content_hash: 'sha256:8e329b21976aa3c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# visibleMapRect

<sub>Instance Property</sub>

The area visible in the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var visibleMapRect: MKMapRect { get set }
```

## Discussion

This property represents the same basic information as the [region](region.md) property but specified as a map rectangle instead of a region.

Changing the value of this property updates the map view immediately. If you want to animate the change, use the [- setVisibleMapRect:animated:](<setvisiblemaprect(__animated_).md>) method instead.

## See Also

### Manipulating the visible portion of the map

- [region](region.md) — The area the map view displays.
- [- setRegion:animated:](<setregion(__animated_).md>) — Changes the currently visible region, and optionally animates the change.
- [centerCoordinate](centercoordinate.md) — The map coordinate at the center of the map view.
- [- setCenterCoordinate:animated:](<setcenter(__animated_).md>) — Changes the center coordinate of the map, and optionally animates the change.
- [- showAnnotations:animated:](<showannotations(__animated_).md>) — Sets the visible region so that the map displays the specified annotations.
- [- setVisibleMapRect:animated:](<setvisiblemaprect(__animated_).md>) — Changes the currently visible portion of the map, and optionally animates the change.
- [- setVisibleMapRect:edgePadding:animated:](<setvisiblemaprect(__edgepadding_animated_).md>) — Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
