---
title: 'addOverlays(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/addoverlays(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/addoverlays(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/addoverlays%28_%3A%29.json'
content_hash: 'sha256:d2433b7d8738bc57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# addOverlays(_:)

<sub>Instance Method</sub>

Adds an array of overlay objects to the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addOverlays(_ overlays: [any MKOverlay])
```

## Parameters

- `overlays` — An array of objects, each of which needs to conform to the [MKOverlay](../mkoverlay.md) protocol.

## Discussion

The map view adds the specified objects to the group of overlay objects in the [MKOverlayLevelAboveLabels](../mkoverlaylevel/abovelabels.md) level. Adding an overlay causes the map view to begin monitoring the area that the overlay represents. As soon as the bounding rectangle of the overlay intersects the visible portion of the map, the map view tries to draw the overlay, or adds the corresponding overlay view to the map. Implement the [- mapView:rendererForOverlay:](<../mkmapviewdelegate/mapview(__rendererfor_).md>) method of the map view’s delegate object to provide the overlay view.

To remove multiple overlays from a map, use the [- removeOverlays:](<removeoverlays(__).md>) method.

## See Also

### Related Documentation

- [- removeOverlay:](<removeoverlay(__).md>) — Removes a single overlay object from the map.
- [- removeOverlays:](<removeoverlays(__).md>) — Removes one or more overlay objects from the map.

### Adding and inserting overlays

- [- addOverlay:level:](<addoverlay(__level_).md>) — Adds the overlay object to the map at the specified level.
- [- addOverlays:level:](<addoverlays(__level_).md>) — Adds an array of overlay objects to the map at the specified level.
- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- insertOverlay:atIndex:level:](<insertoverlay(__at_level_).md>) — Inserts an overlay object into the level at the specified index.
- [- insertOverlay:atIndex:](<insertoverlay(__at_).md>) — Inserts an overlay object into the list associated with the map.
- [- insertOverlay:aboveOverlay:](<insertoverlay(__above_).md>) — Inserts one overlay object above another.
- [- insertOverlay:belowOverlay:](<insertoverlay(__below_).md>) — Inserts one overlay object below another.
- [- exchangeOverlay:withOverlay:](<exchangeoverlay(__with_).md>) — Exchanges the positions of two overlay objects.
- [- exchangeOverlayAtIndex:withOverlayAtIndex:](<exchangeoverlay(at_withoverlayat_).md>) — Exchanges the position of two overlay objects at the specified index.
