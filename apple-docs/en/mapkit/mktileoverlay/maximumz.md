---
title: maximumZ
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlay/maximumz
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/maximumz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/maximumz.json'
content_hash: 'sha256:bb322b060f7d8c53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# maximumZ

<sub>Instance Property</sub>

The maximum zoom level that the tiles of this overlay object support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maximumZ: Int { get set }
```

## Discussion

If you use different overlay objects to represent different tiles at different zoom levels, use this property to specify the maximum zoom level that this overlay’s tiles support. At zoom level 0, tiles cover the entire world map; at zoom level 1, tiles cover 1/4 of the world; at zoom level 2, tiles cover 1/16 of the world, and so on. The map doesn’t attempt to load tiles for a zoom level greater than the value that this property specifies.

The default value of this property is `21`. Setting the value of this property to a number greater than the default doesn’t ensure the use of those extra zoom levels.

## See Also

### Accessing the tile attributes

- [tileSize](tilesize.md) — The size (in pixels) of your tile images.
- [geometryFlipped](isgeometryflipped.md) — A Boolean value that indicates the orientation of tile indexes along the y-axis.
- [minimumZ](minimumz.md) — The minimum zoom level that the tiles of this overlay object support.
- [canReplaceMapContent](canreplacemapcontent.md) — A Boolean value that indicates whether the tile content is fully opaque.
