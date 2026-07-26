---
title: 'init(tileOverlay:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mktileoverlayrenderer/init(tileoverlay:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/init(tileoverlay:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlayrenderer/init%28tileoverlay%3A%29.json'
content_hash: 'sha256:35de71686422e6aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlayRenderer](../mktileoverlayrenderer.md)

# init(tileOverlay:)

<sub>Initializer</sub>

Initializes and returns a tile renderer with the specified overlay object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(tileOverlay overlay: MKTileOverlay)
```

## Parameters

- `overlay` — The tile overlay object whose contents you want to draw.

## Return Value

An initialized tile renderer object.

## Discussion

The returned renderer object works with the tile overlay object to coordinate the loading and display of its map tiles.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
