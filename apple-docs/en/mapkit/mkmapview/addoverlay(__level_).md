---
title: 'addOverlay(_:level:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/addoverlay(_:level:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/addoverlay(_:level:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/addoverlay%28_%3Alevel%3A%29.json'
content_hash: 'sha256:313afe84330a4808'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# addOverlay(_:level:)

<sub>Instance Method</sub>

Adds the overlay object to the map at the specified level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addOverlay(_ overlay: any MKOverlay, level: MKOverlayLevel)
```

## Parameters

- `overlay` — The overlay object to add. This object needs to conform to the [MKOverlay](../mkoverlay.md) protocol.

- `level` — The map level at which to place the overlay. For a list of possible values for this parameter, see [MKOverlayLevel](../mkoverlaylevel.md).

## Discussion

Positioning an overlay at a specific level places that overlay’s visual representation in front of or behind other map content such as map labels and point-of-interest icons.

This method adds the specified overlay to the end of the list of overlay objects at the given level. Adding an overlay also causes the map view to begin monitoring the area they represent. As soon as the bounding rectangle of the overlay intersects the visible portion of the map, the map view calls your delegate’s [- mapView:rendererForOverlay:](<../mkmapviewdelegate/mapview(__rendererfor_).md>) method to get the renderer object to use when drawing the overlay.

To remove an overlay from a map, use the [- removeOverlay:](<removeoverlay(__).md>) method.

## See Also

### Adding and inserting overlays

- [- addOverlays:level:](<addoverlays(__level_).md>) — Adds an array of overlay objects to the map at the specified level.
- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- addOverlays:](<addoverlays(__).md>) — Adds an array of overlay objects to the map.
- [- insertOverlay:atIndex:level:](<insertoverlay(__at_level_).md>) — Inserts an overlay object into the level at the specified index.
- [- insertOverlay:atIndex:](<insertoverlay(__at_).md>) — Inserts an overlay object into the list associated with the map.
- [- insertOverlay:aboveOverlay:](<insertoverlay(__above_).md>) — Inserts one overlay object above another.
- [- insertOverlay:belowOverlay:](<insertoverlay(__below_).md>) — Inserts one overlay object below another.
- [- exchangeOverlay:withOverlay:](<exchangeoverlay(__with_).md>) — Exchanges the positions of two overlay objects.
- [- exchangeOverlayAtIndex:withOverlayAtIndex:](<exchangeoverlay(at_withoverlayat_).md>) — Exchanges the position of two overlay objects at the specified index.
