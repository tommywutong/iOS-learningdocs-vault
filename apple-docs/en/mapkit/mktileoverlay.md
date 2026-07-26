---
title: MKTileOverlay
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlay
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay.json'
content_hash: 'sha256:251777014823dc44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKTileOverlay

<sub>Class</sub>

An overlay that covers an area of the map with tiles of bitmap images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKTileOverlay
```

## Overview

You use tile overlay objects to represent your own tile-based content and to coordinate the display of that content in a map view. Your tiles can supplement the underlying map content or replace it completely. A tile overlay object coordinates the loading and management of the tiles, and a corresponding [MKTileOverlayRenderer](mktileoverlayrenderer.md) object handles the actual drawing of the tiles on the map.

You can use a single tile overlay object to represent all of the tiles at one or more zoom levels of the map. The default tile overlay object uses a template string to build URLs so that it can locate the map tiles it needs. Each URL incorporates the x and y index of the map tile, the zoom level it’s intended for, and the scale factor corresponding to the screen resolution on which to display the tile. The default class lets you specify map tiles with indexes that start in either the upper-left corner or lower-left corner of the map. If you use a different indexing scheme for your tiles, you can also subclass and override the [- URLForTilePath:](<mktileoverlay/url(fortilepath_).md>) or [- loadTileAtPath:result:](<mktileoverlay/loadtile(at_result_).md>) methods to map between the requested tile and your custom indexing scheme.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKOverlay](mkoverlay.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a tile overlay

- [- initWithURLTemplate:](<mktileoverlay/init(urltemplate_)-9s8h7.md>) — Creates and returns a tile overlay object using the specified tile-access template.

### Accessing the tile attributes

- [tileSize](mktileoverlay/tilesize.md) — The size (in pixels) of your tile images.
- [geometryFlipped](mktileoverlay/isgeometryflipped.md) — A Boolean value that indicates the orientation of tile indexes along the y-axis.
- [minimumZ](mktileoverlay/minimumz.md) — The minimum zoom level that the tiles of this overlay object support.
- [maximumZ](mktileoverlay/maximumz.md) — The maximum zoom level that the tiles of this overlay object support.
- [canReplaceMapContent](mktileoverlay/canreplacemapcontent.md) — A Boolean value that indicates whether the tile content is fully opaque.

### Customizing the loading of tiles

- [URLTemplate](mktileoverlay/urltemplate.md) — The template for generating tile image URLs.
- [- URLForTilePath:](<mktileoverlay/url(fortilepath_).md>) — Returns the URL to use to access the specified tile.
- [- loadTileAtPath:result:](<mktileoverlay/loadtile(at_result_).md>) — Loads the specified tile asynchronously.
- [MKTileOverlayPath](mktileoverlaypath.md) — Values that specify the path indexes for a single overlay tile.

### Initializers

- [init(URLTemplate:)](<mktileoverlay/init(urltemplate_)-1wri0.md>)

## See Also

### Tiled image overlays

- [MKTileOverlayRenderer](mktileoverlayrenderer.md) — The renderer for a tile overlay that handles the drawing of bitmap images on the map surface.
