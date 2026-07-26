---
title: urlTemplate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlay/urltemplate
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/urltemplate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/urltemplate.json'
content_hash: 'sha256:2f6335518f508bed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# urlTemplate

<sub>Instance Property</sub>

The template for generating tile image URLs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var urlTemplate: String? { get }
```

## Discussion

You specify this string at initialization time.

## See Also

### Related Documentation

- [- initWithURLTemplate:](<init(urltemplate_)-9s8h7.md>) — Creates and returns a tile overlay object using the specified tile-access template.

### Customizing the loading of tiles

- [- URLForTilePath:](<url(fortilepath_).md>) — Returns the URL to use to access the specified tile.
- [- loadTileAtPath:result:](<loadtile(at_result_).md>) — Loads the specified tile asynchronously.
- [MKTileOverlayPath](../mktileoverlaypath.md) — Values that specify the path indexes for a single overlay tile.
