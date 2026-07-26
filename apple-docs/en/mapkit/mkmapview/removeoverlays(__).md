---
title: 'removeOverlays(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/removeoverlays(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/removeoverlays(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/removeoverlays%28_%3A%29.json'
content_hash: 'sha256:b13e63629ca5e1ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# removeOverlays(_:)

<sub>Instance Method</sub>

Removes one or more overlay objects from the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeOverlays(_ overlays: [any MKOverlay])
```

## Parameters

- `overlays` — An array of objects, each of which conforms to the [MKOverlay](../mkoverlay.md) protocol.

## Discussion

This method removes the specified overlays regardless of which level each one is in. Removing an overlay also removes its corresponding renderer, if one is in use. The method ignores an overlay object if it isn’t associated with the map view.

## See Also

### Related Documentation

- [- addOverlay:](<addoverlay(__).md>) — Adds a single overlay object to the map.
- [- addOverlays:](<addoverlays(__).md>) — Adds an array of overlay objects to the map.

### Removing overlays

- [- removeOverlay:](<removeoverlay(__).md>) — Removes a single overlay object from the map.
