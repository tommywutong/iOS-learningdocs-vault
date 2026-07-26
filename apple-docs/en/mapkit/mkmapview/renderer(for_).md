---
title: 'renderer(for:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/renderer(for:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/renderer(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/renderer%28for%3A%29.json'
content_hash: 'sha256:00ac32060b89644b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# renderer(for:)

<sub>Instance Method</sub>

Returns the renderer object for drawing the contents of the specified overlay object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func renderer(for overlay: any MKOverlay) -> MKOverlayRenderer?
```

## Parameters

- `overlay` — The overlay object whose renderer you want.

## Return Value

The renderer object in use for the specified overlay or `nil` if the overlay is not onscreen.

## Discussion

This method returns the renderer object that your map delegate provided in its [- mapView:rendererForOverlay:](<../mkmapviewdelegate/mapview(__rendererfor_).md>) method.

## See Also

### Accessing overlays

- [overlays](overlays.md) — The overlay objects associated with the map view.
- [- overlaysInLevel:](<overlays(in_).md>) — Returns overlay objects in the specified level of the map.
- [MKOverlayLevel](../mkoverlaylevel.md) — Constants that indicate the position of overlays relative to other content.
- [- viewForOverlay:](<view(for_)-38z60.md>) — Returns the view associated with the overlay object, if any. _(deprecated)_
