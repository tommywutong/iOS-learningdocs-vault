---
title: reloadData()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mktileoverlayrenderer/reloaddata()
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/reloaddata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlayrenderer/reloaddata%28%29.json'
content_hash: 'sha256:f4e2d77b5847f51c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlayRenderer](../mktileoverlayrenderer.md)

# reloadData()

<sub>Instance Method</sub>

Forces the tile overlay renderer to reload and redisplay the tiles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reloadData()
```

## Discussion

Use this method to remove the overlay’s existing tile images and reload them from the original source. This method automatically causes the renderer to redraw the new tiles as soon as it loads them into memory.
