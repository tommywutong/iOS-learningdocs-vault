---
title: 'url(forTilePath:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mktileoverlay/url(fortilepath:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/url(fortilepath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/url%28fortilepath%3A%29.json'
content_hash: 'sha256:e3052a31490cec46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# url(forTilePath:)

<sub>Instance Method</sub>

Returns the URL to use to access the specified tile.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func url(forTilePath path: MKTileOverlayPath) -> URL
```

## Parameters

- `path` — The path structure that identifies the specific tile you want. This structure incorporates the tile’s x-y coordinate at a given zoom level and scale factor.

## Return Value

The URL to use to retrieve the tile.

## Discussion

The default implementation of this method uses the template string you provide at initialization time to build a URL to the specified tile image. Subclasses can override this method and use a different scheme to provide URLs for tiles. You can locate the tiles either on a local file system or on a remote server.

## See Also

### Related Documentation

- [- initWithURLTemplate:](<init(urltemplate_)-9s8h7.md>) — Creates and returns a tile overlay object using the specified tile-access template.

### Customizing the loading of tiles

- [URLTemplate](urltemplate.md) — The template for generating tile image URLs.
- [- loadTileAtPath:result:](<loadtile(at_result_).md>) — Loads the specified tile asynchronously.
- [MKTileOverlayPath](../mktileoverlaypath.md) — Values that specify the path indexes for a single overlay tile.
