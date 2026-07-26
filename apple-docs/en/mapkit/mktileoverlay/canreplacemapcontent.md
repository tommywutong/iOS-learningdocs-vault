---
title: canReplaceMapContent
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlay/canreplacemapcontent
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/canreplacemapcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/canreplacemapcontent.json'
content_hash: 'sha256:8c2ac1f275535f26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# canReplaceMapContent

<sub>Instance Property</sub>

A Boolean value that indicates whether the tile content is fully opaque.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var canReplaceMapContent: Bool { get set }
```

## Discussion

If the tile content you provide can cover the entire drawing area with opaque content, set this property to [true](../../swift/true.md). Doing so serves as a hint to the map view that it doesn’t need to draw any additional content underneath your tiles. Set this property to [false](../../swift/false.md) if your tiles contain any transparency.

The default value for this property is [false](../../swift/false.md).

## See Also

### Accessing the tile attributes

- [tileSize](tilesize.md) — The size (in pixels) of your tile images.
- [geometryFlipped](isgeometryflipped.md) — A Boolean value that indicates the orientation of tile indexes along the y-axis.
- [minimumZ](minimumz.md) — The minimum zoom level that the tiles of this overlay object support.
- [maximumZ](maximumz.md) — The maximum zoom level that the tiles of this overlay object support.
