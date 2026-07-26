---
title: contentScaleFactor
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlayrenderer/contentscalefactor
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/contentscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/contentscalefactor.json'
content_hash: 'sha256:c264ffc91d697566'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# contentScaleFactor

<sub>Instance Property</sub>

The scale factor for drawing the overlay’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentScaleFactor: CGFloat { get }
```

## Discussion

The scale factor determines how the overlay renders map content from the logical coordinate space (in points) to the device coordinate space (in pixels). This value is typically either `1.0` or `2.0`. Higher scale factors indicate that each point represents more than one pixel on the screen. For example, if the scale factor is `2.0` and the drawing rectangle size is 50 x 50 points, the size of the underlying area is 100 x 100 pixels.

When drawing the content for your overlays, you can use this value to determine how best to render your content.

## See Also

### Attributes of the overlay

- [overlay](overlay.md) — The overlay object containing the data for drawing.
- [alpha](alpha.md) — The amount of transparency to apply to the overlay.
- [blendMode](blendmode.md) — The blend mode to apply to the overlay.
