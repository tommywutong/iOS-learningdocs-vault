---
title: 'loadTile(at:result:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mktileoverlay/loadtile(at:result:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/loadtile(at:result:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/loadtile%28at%3Aresult%3A%29.json'
content_hash: 'sha256:ed5a06d2eee058c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# loadTile(at:result:)

<sub>Instance Method</sub>

Loads the specified tile asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func loadTile(at path: MKTileOverlayPath, result: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func loadTile(at path: MKTileOverlayPath) async throws -> Data
```

## Parameters

- `path` — The path structure that identifies the specific tile you want. This structure incorporates the tile’s x-y coordinate at a given zoom level and scale factor.

- `result` — The completion block to call when the tile data is available. The method can execute this block on any queue and takes the following parameters: - The `tileData` parameter contains the raw data that loads from the corresponding image file. You can use this data to initialize an image object. If an error occurs, this parameter is `nil`. - The `error` parameter contains an error object if there is a problem loading the tile image. If no errors occur, this parameter is `nil`.

## Discussion

The default implementation of this method uses the [- URLForTilePath:](<url(fortilepath_).md>) method to retrieve the URL for the specified tile and then loads that tile into memory asynchronously using a [URLSession](../../foundation/urlsession.md) object. The specified tile may be located either on the local file system or on a remote server. Subclasses may override this method and implement their own custom tile-loading behavior.

When a tile overlay renderer (that is, an instance of [MKTileOverlayRenderer](../mktileoverlayrenderer.md)) needs to display tiles, it uses this method to request the data for each tile.

## See Also

### Customizing the loading of tiles

- [URLTemplate](urltemplate.md) — The template for generating tile image URLs.
- [- URLForTilePath:](<url(fortilepath_).md>) — Returns the URL to use to access the specified tile.
- [MKTileOverlayPath](../mktileoverlaypath.md) — Values that specify the path indexes for a single overlay tile.
