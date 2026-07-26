---
title: overlay
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlayrenderer/overlay
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/overlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/overlay.json'
content_hash: 'sha256:46a5b1fb0356ca5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# overlay

<sub>Instance Property</sub>

The overlay object containing the data for drawing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var overlay: any MKOverlay { get }
```

## Discussion

The overlay object contains the coordinate at which to draw the overlay and other information that your app provides.

## See Also

### Attributes of the overlay

- [alpha](alpha.md) — The amount of transparency to apply to the overlay.
- [contentScaleFactor](contentscalefactor.md) — The scale factor for drawing the overlay’s content.
- [blendMode](blendmode.md) — The blend mode to apply to the overlay.
