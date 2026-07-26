---
title: 'overlays(in:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/overlays(in:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/overlays(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/overlays%28in%3A%29.json'
content_hash: 'sha256:8e5e73ed66af4ece'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# overlays(in:)

<sub>Instance Method</sub>

Returns overlay objects in the specified level of the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func overlays(in level: MKOverlayLevel) -> [any MKOverlay]
```

## Parameters

- `level` — The map level whose overlays you want. For a list of possible values for this parameter, see [MKOverlayLevel](../mkoverlaylevel.md).

## Return Value

An array of objects conforming to the [MKOverlay](../mkoverlay.md) protocol that display in the specified map level. If there are no overlays at the specified level, this method returns an empty array.

## Discussion

You can use this method to get all of the overlays assigned to a specific map level, which might be a subset of the complete set of overlay objects. For overlapping overlay objects, the order of objects in the array represents their visual order when displayed on the map, with objects in the beginning of the array located behind those at later indexes.

## See Also

### Related Documentation

- [- addOverlays:level:](<addoverlays(__level_).md>) — Adds an array of overlay objects to the map at the specified level.
- [- addOverlay:level:](<addoverlay(__level_).md>) — Adds the overlay object to the map at the specified level.

### Accessing overlays

- [overlays](overlays.md) — The overlay objects associated with the map view.
- [- rendererForOverlay:](<renderer(for_).md>) — Returns the renderer object for drawing the contents of the specified overlay object.
- [MKOverlayLevel](../mkoverlaylevel.md) — Constants that indicate the position of overlays relative to other content.
- [- viewForOverlay:](<view(for_)-38z60.md>) — Returns the view associated with the overlay object, if any. _(deprecated)_
