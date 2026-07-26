---
title: 'insertOverlay(_:at:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/insertoverlay(_:at:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/insertoverlay(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/insertoverlay%28_%3Aat%3A%29.json'
content_hash: 'sha256:e0b1ee39b6e15b1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# insertOverlay(_:at:)

<sub>Instance Method</sub>

Inserts an overlay object into the list associated with the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertOverlay(_ overlay: any MKOverlay, at index: Int)
```

## Parameters

- `overlay` — The overlay object to insert.

- `index` — The index at which to insert the overlay object. If this value is greater than the number of objects in the [overlays](overlays.md) property, this method appends the object to the end of the array.

## Discussion

This method inserts the overlay into the [MKOverlayLevelAboveLabels](../mkoverlaylevel/abovelabels.md) level.

## See Also

### Adding and inserting overlays

- [- addOverlay:level:](<addoverlay(__level_).md>) — Adds the overlay object to the map at the specified level.
- [- addOverlays:level:](<addoverlays(__level_).md>) — Adds an array of overlay objects to the map at the specified level.
- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- addOverlays:](<addoverlays(__).md>) — Adds an array of overlay objects to the map.
- [- insertOverlay:atIndex:level:](<insertoverlay(__at_level_).md>) — Inserts an overlay object into the level at the specified index.
- [- insertOverlay:aboveOverlay:](<insertoverlay(__above_).md>) — Inserts one overlay object above another.
- [- insertOverlay:belowOverlay:](<insertoverlay(__below_).md>) — Inserts one overlay object below another.
- [- exchangeOverlay:withOverlay:](<exchangeoverlay(__with_).md>) — Exchanges the positions of two overlay objects.
- [- exchangeOverlayAtIndex:withOverlayAtIndex:](<exchangeoverlay(at_withoverlayat_).md>) — Exchanges the position of two overlay objects at the specified index.
