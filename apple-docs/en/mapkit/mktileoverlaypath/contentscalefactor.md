---
title: contentScaleFactor
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlaypath/contentscalefactor
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlaypath/contentscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlaypath/contentscalefactor.json'
content_hash: 'sha256:8b5bf23e7ac64339'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlayPath](../mktileoverlaypath.md)

# contentScaleFactor

<sub>Instance Property</sub>

The tile’s intended screen scale factor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentScaleFactor: CGFloat
```

## Discussion

This value is typically either `1.0` (for standard resolution displays) or `2.0` (for Retina displays).

## See Also

### Instance properties

- [x](x.md) — The index of the tile along the x-axis of the map.
- [y](y.md) — The index of the tile along the y-axis of the map.
- [z](z.md) — The index of the tile along the z-axis of the map.
