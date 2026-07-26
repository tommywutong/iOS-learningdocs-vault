---
title: overlays
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/overlays
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/overlays'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/overlays.json'
content_hash: 'sha256:5e2aeee685048f15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# overlays

<sub>Instance Property</sub>

The overlay objects associated with the map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var overlays: [any MKOverlay] { get }
```

## Discussion

This property contains the union of all overlays at the different levels of the map. The objects in this array adopt the [MKOverlay](../mkoverlay.md) protocol. If the map view has no associated no overlays, the value of this property is an empty array.

The order of the objects in this array doesn’t necessarily reflect their visual order on the map.

## See Also

### Accessing overlays

- [- overlaysInLevel:](<overlays(in_).md>) — Returns overlay objects in the specified level of the map.
- [- rendererForOverlay:](<renderer(for_).md>) — Returns the renderer object for drawing the contents of the specified overlay object.
- [MKOverlayLevel](../mkoverlaylevel.md) — Constants that indicate the position of overlays relative to other content.
- [- viewForOverlay:](<view(for_)-38z60.md>) — Returns the view associated with the overlay object, if any. _(deprecated)_
