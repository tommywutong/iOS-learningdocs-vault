---
title: isGeometryFlipped
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlay/isgeometryflipped
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/isgeometryflipped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/isgeometryflipped.json'
content_hash: 'sha256:b0ecc31c17c935e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# isGeometryFlipped

<sub>Instance Property</sub>

A Boolean value that indicates the orientation of tile indexes along the y-axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isGeometryFlipped: Bool { get set }
```

## Discussion

When set to [false](../../swift/false.md), tile indexes start in the upper-left corner of the map and proceed down and to the right. Thus, the tile at `(0, 0)`is in the upper-left corner of the map, the tile at `(1, 0)` is to its immediate right and the tile at `(0, 1)` is immediately below it. Setting this property to [true](../../swift/true.md) causes the map to start indexes at the lower-left corner of the map and proceed up and to the right.

The default value of this property is [false](../../swift/false.md).

## See Also

### Accessing the tile attributes

- [tileSize](tilesize.md) — The size (in pixels) of your tile images.
- [minimumZ](minimumz.md) — The minimum zoom level that the tiles of this overlay object support.
- [maximumZ](maximumz.md) — The maximum zoom level that the tiles of this overlay object support.
- [canReplaceMapContent](canreplacemapcontent.md) — A Boolean value that indicates whether the tile content is fully opaque.
