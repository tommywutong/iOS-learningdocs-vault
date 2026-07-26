---
title: 'insertOverlay(_:at:level:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/insertoverlay(_:at:level:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/insertoverlay(_:at:level:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/insertoverlay%28_%3Aat%3Alevel%3A%29.json'
content_hash: 'sha256:0fec3cd024176bc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# insertOverlay(_:at:level:)

<sub>Instance Method</sub>

Inserts an overlay object into the level at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertOverlay(_ overlay: any MKOverlay, at index: Int, level: MKOverlayLevel)
```

## Parameters

- `overlay` — The overlay object to insert.

- `index` — The index at which to insert the overlay object. If this value is greater than the number of objects in the [overlays](overlays.md) property, this method appends the object to the end of the array.

- `level` — The map level at which to place the overlay. For a list of possible values for this parameter, see [MKOverlayLevel](../mkoverlaylevel.md).

## Discussion

Inserting an overlay at a specific level places that overlay’s visual representation in front of or behind other map content such as map labels and point-of-interest icons.

## See Also

### Adding and inserting overlays

- [- addOverlay:level:](<addoverlay(__level_).md>) — Adds the overlay object to the map at the specified level.
- [- addOverlays:level:](<addoverlays(__level_).md>) — Adds an array of overlay objects to the map at the specified level.
- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- addOverlays:](<addoverlays(__).md>) — Adds an array of overlay objects to the map.
- [- insertOverlay:atIndex:](<insertoverlay(__at_).md>) — Inserts an overlay object into the list associated with the map.
- [- insertOverlay:aboveOverlay:](<insertoverlay(__above_).md>) — Inserts one overlay object above another.
- [- insertOverlay:belowOverlay:](<insertoverlay(__below_).md>) — Inserts one overlay object below another.
- [- exchangeOverlay:withOverlay:](<exchangeoverlay(__with_).md>) — Exchanges the positions of two overlay objects.
- [- exchangeOverlayAtIndex:withOverlayAtIndex:](<exchangeoverlay(at_withoverlayat_).md>) — Exchanges the position of two overlay objects at the specified index.
