---
title: minimumZ
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlay/minimumz
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/minimumz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/minimumz.json'
content_hash: 'sha256:ef9b88f37fa3d6b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# minimumZ

<sub>Instance Property</sub>

The minimum zoom level that the tiles of this overlay object support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var minimumZ: Int { get set }
```

## Discussion

If you use different overlay objects to represent different tiles at different zoom levels, use this property to specify the minimum zoom level supported by this overlay’s tiles. At zoom level 0, tiles cover the entire world map; at zoom level 1, tiles cover 1/4 of the world; at zoom level 2, tiles cover 1/16 of the world, and so on. The map never tries to load tiles for a zoom level less than the value specified by this property.

The default value of this property is `0`.

## See Also

### Accessing the tile attributes

- [tileSize](tilesize.md) — The size (in pixels) of your tile images.
- [geometryFlipped](isgeometryflipped.md) — A Boolean value that indicates the orientation of tile indexes along the y-axis.
- [maximumZ](maximumz.md) — The maximum zoom level that the tiles of this overlay object support.
- [canReplaceMapContent](canreplacemapcontent.md) — A Boolean value that indicates whether the tile content is fully opaque.
