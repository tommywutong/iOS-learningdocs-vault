---
title: tileSize
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlay/tilesize
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/tilesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/tilesize.json'
content_hash: 'sha256:6d2a788c906708a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# tileSize

<sub>Instance Property</sub>

The size (in pixels) of your tile images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var tileSize: CGSize { get set }
```

## Discussion

On Retina displays, the system renders images pixel for pixel and doesn’t scale them. This means that if the tile size is 256 x 256 pixels and the scale factor is `2.0`, the system renders the image as if it is 128 x 128 points in size. This behavior causes the tile to appear smaller, but preserves the original image data.

The default tile size is 256 x 256 pixels.

## See Also

### Accessing the tile attributes

- [geometryFlipped](isgeometryflipped.md) — A Boolean value that indicates the orientation of tile indexes along the y-axis.
- [minimumZ](minimumz.md) — The minimum zoom level that the tiles of this overlay object support.
- [maximumZ](maximumz.md) — The maximum zoom level that the tiles of this overlay object support.
- [canReplaceMapContent](canreplacemapcontent.md) — A Boolean value that indicates whether the tile content is fully opaque.
