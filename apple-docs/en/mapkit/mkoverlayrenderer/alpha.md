---
title: alpha
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlayrenderer/alpha
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/alpha'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/alpha.json'
content_hash: 'sha256:da8a135863cc07c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# alpha

<sub>Instance Property</sub>

The amount of transparency to apply to the overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var alpha: CGFloat { get set }
```

## Discussion

The value in this property can be in the range `0.0` to `1.0`, where `0.0` represents total transparency and `1.0` represents total opacity. The default value of this property is `1.0`.

## See Also

### Attributes of the overlay

- [overlay](overlay.md) — The overlay object containing the data for drawing.
- [contentScaleFactor](contentscalefactor.md) — The scale factor for drawing the overlay’s content.
- [blendMode](blendmode.md) — The blend mode to apply to the overlay.
