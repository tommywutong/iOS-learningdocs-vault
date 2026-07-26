---
title: blendMode
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlayrenderer/blendmode
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/blendmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/blendmode.json'
content_hash: 'sha256:e1b702145750efbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# blendMode

<sub>Instance Property</sub>

The blend mode to apply to the overlay.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var blendMode: CGBlendMode { get set }
```

## Discussion

Choose the blend mode from one of the possible [CGBlendMode](../../coregraphics/cgblendmode.md) enumerations.

## See Also

### Attributes of the overlay

- [overlay](overlay.md) — The overlay object containing the data for drawing.
- [alpha](alpha.md) — The amount of transparency to apply to the overlay.
- [contentScaleFactor](contentscalefactor.md) — The scale factor for drawing the overlay’s content.
