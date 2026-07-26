---
title: 'exchangeOverlay(at:withOverlayAt:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/exchangeoverlay(at:withoverlayat:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/exchangeoverlay(at:withoverlayat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/exchangeoverlay%28at%3Awithoverlayat%3A%29.json'
content_hash: 'sha256:e3ccd52b2180cde8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# exchangeOverlay(at:withOverlayAt:)

<sub>Instance Method</sub>

Exchanges the position of two overlay objects at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func exchangeOverlay(at index1: Int, withOverlayAt index2: Int)
```

## Parameters

- `index1` — The index of an overlay in the [MKOverlayLevelAboveLabels](../mkoverlaylevel/abovelabels.md) map level.

- `index2` — The index of another overlay in the [MKOverlayLevelAboveLabels](../mkoverlaylevel/abovelabels.md) map level.

## Discussion

If you need to exchange overlays in other map levels, use the [- exchangeOverlay:withOverlay:](<exchangeoverlay(__with_).md>) method.

## See Also

### Adding and inserting overlays

- [- addOverlay:level:](<addoverlay(__level_).md>) — Adds the overlay object to the map at the specified level.
- [- addOverlays:level:](<addoverlays(__level_).md>) — Adds an array of overlay objects to the map at the specified level.
- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- addOverlays:](<addoverlays(__).md>) — Adds an array of overlay objects to the map.
- [- insertOverlay:atIndex:level:](<insertoverlay(__at_level_).md>) — Inserts an overlay object into the level at the specified index.
- [- insertOverlay:atIndex:](<insertoverlay(__at_).md>) — Inserts an overlay object into the list associated with the map.
- [- insertOverlay:aboveOverlay:](<insertoverlay(__above_).md>) — Inserts one overlay object above another.
- [- insertOverlay:belowOverlay:](<insertoverlay(__below_).md>) — Inserts one overlay object below another.
- [- exchangeOverlay:withOverlay:](<exchangeoverlay(__with_).md>) — Exchanges the positions of two overlay objects.
