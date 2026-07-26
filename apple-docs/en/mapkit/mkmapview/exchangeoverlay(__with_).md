---
title: 'exchangeOverlay(_:with:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/exchangeoverlay(_:with:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/exchangeoverlay(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/exchangeoverlay%28_%3Awith%3A%29.json'
content_hash: 'sha256:c191d3638b74f946'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# exchangeOverlay(_:with:)

<sub>Instance Method</sub>

Exchanges the positions of two overlay objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func exchangeOverlay(_ overlay1: any MKOverlay, with overlay2: any MKOverlay)
```

## Parameters

- `overlay1` — The first overlay object.

- `overlay2` — The second overlay object.

## Discussion

If the overlays are in the same map level, they exchange positions within that level’s array of overlay objects. If they’re in different map levels, the two objects also swap levels. Swapping the position of the overlays affects their visibility in the map view.

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
- [- exchangeOverlayAtIndex:withOverlayAtIndex:](<exchangeoverlay(at_withoverlayat_).md>) — Exchanges the position of two overlay objects at the specified index.
