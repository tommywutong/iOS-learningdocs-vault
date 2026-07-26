---
title: MKTileOverlayPath
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlaypath
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlaypath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlaypath.json'
content_hash: 'sha256:f30e62de675229fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKTileOverlayPath

<sub>Structure</sub>

Values that specify the path indexes for a single overlay tile.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MKTileOverlayPath
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a tile overlay path

- [init()](<mktileoverlaypath/init().md>) — Creates a new tile overlay path.
- [init(x:y:z:contentScaleFactor:)](<mktileoverlaypath/init(x_y_z_contentscalefactor_).md>) — Creates a new overlay path with the specified indexes and content scale factor.

### Instance properties

- [x](mktileoverlaypath/x.md) — The index of the tile along the x-axis of the map.
- [y](mktileoverlaypath/y.md) — The index of the tile along the y-axis of the map.
- [z](mktileoverlaypath/z.md) — The index of the tile along the z-axis of the map.
- [contentScaleFactor](mktileoverlaypath/contentscalefactor.md) — The tile’s intended screen scale factor.

## See Also

### Customizing the loading of tiles

- [URLTemplate](mktileoverlay/urltemplate.md) — The template for generating tile image URLs.
- [- URLForTilePath:](<mktileoverlay/url(fortilepath_).md>) — Returns the URL to use to access the specified tile.
- [- loadTileAtPath:result:](<mktileoverlay/loadtile(at_result_).md>) — Loads the specified tile asynchronously.
