---
title: 'insertOverlay(_:below:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/insertoverlay(_:below:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/insertoverlay(_:below:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/insertoverlay%28_%3Abelow%3A%29.json'
content_hash: 'sha256:de965e53200d6c50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# insertOverlay(_:below:)

<sub>Instance Method</sub>

Inserts one overlay object below another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertOverlay(_ overlay: any MKOverlay, below sibling: any MKOverlay)
```

## Parameters

- `overlay` — The overlay object to insert.

- `sibling` — An existing object in the [overlays](overlays.md) array. This object needs to exist in the array and can’t be `nil`.

## Discussion

This method inserts the overlay into the [MKOverlayLevelAboveLabels](../mkoverlaylevel/abovelabels.md) level and positions it relative to the specified sibling. When displaying it, the map view displays the overlay’s contents beneath that of its sibling. If the sibling isn’t in the same map level, this method appends the overlay to the end of the list of overlays at the indicated level.

## See Also

### Adding and inserting overlays

- [- addOverlay:level:](<addoverlay(__level_).md>) — Adds the overlay object to the map at the specified level.
- [- addOverlays:level:](<addoverlays(__level_).md>) — Adds an array of overlay objects to the map at the specified level.
- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- addOverlays:](<addoverlays(__).md>) — Adds an array of overlay objects to the map.
- [- insertOverlay:atIndex:level:](<insertoverlay(__at_level_).md>) — Inserts an overlay object into the level at the specified index.
- [- insertOverlay:atIndex:](<insertoverlay(__at_).md>) — Inserts an overlay object into the list associated with the map.
- [- insertOverlay:aboveOverlay:](<insertoverlay(__above_).md>) — Inserts one overlay object above another.
- [- exchangeOverlay:withOverlay:](<exchangeoverlay(__with_).md>) — Exchanges the positions of two overlay objects.
- [- exchangeOverlayAtIndex:withOverlayAtIndex:](<exchangeoverlay(at_withoverlayat_).md>) — Exchanges the position of two overlay objects at the specified index.
