---
title: 'removeOverlay(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/removeoverlay(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/removeoverlay(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/removeoverlay%28_%3A%29.json'
content_hash: 'sha256:49abd0c783afa727'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# removeOverlay(_:)

<sub>Instance Method</sub>

Removes a single overlay object from the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeOverlay(_ overlay: any MKOverlay)
```

## Parameters

- `overlay` — The overlay object to remove.

## Discussion

This method removes the overlay regardless of the level that it’s in. Removing an overlay also removes its corresponding renderer, if one is in use. If the specified overlay isn’t associated with the map view, this method does nothing.

## See Also

### Related Documentation

- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- addOverlays:](<addoverlays(__).md>) — Adds an array of overlay objects to the map.

### Removing overlays

- [- removeOverlays:](<removeoverlays(__).md>) — Removes one or more overlay objects from the map.
