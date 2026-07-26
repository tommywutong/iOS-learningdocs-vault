---
title: MKTileOverlayRenderer
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlayrenderer
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlayrenderer.json'
content_hash: 'sha256:de523b854d45e774'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKTileOverlayRenderer

<sub>Class</sub>

The renderer for a tile overlay that handles the drawing of bitmap images on the map surface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKTileOverlayRenderer
```

## Overview

You create instances of this class when tile overlays become visible on the map view. A renderer works closely with its associated tile overlay object to coordinate the loading and drawing of tiles at appropriate times.

For information about how to specify the tiles to display on the map, see [MKTileOverlay](mktileoverlay.md).

## Relationships

- **Inherits From**: [MKOverlayRenderer](mkoverlayrenderer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a tile renderer

- [- initWithTileOverlay:](<mktileoverlayrenderer/init(tileoverlay_).md>) — Initializes and returns a tile renderer with the specified overlay object.

### Reloading the tile data

- [- reloadData](<mktileoverlayrenderer/reloaddata().md>) — Forces the tile overlay renderer to reload and redisplay the tiles.

## See Also

### Tiled image overlays

- [MKTileOverlay](mktileoverlay.md) — An overlay that covers an area of the map with tiles of bitmap images.
