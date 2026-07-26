---
title: 'init(urlTemplate:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mktileoverlay/init(urltemplate:)-9s8h7'
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlay/init(urltemplate:)-9s8h7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlay/init%28urltemplate%3A%29-9s8h7.json'
content_hash: 'sha256:b71b97fa82805c48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlay](../mktileoverlay.md)

# init(urlTemplate:)

<sub>Initializer</sub>

Creates and returns a tile overlay object using the specified tile-access template.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(urlTemplate URLTemplate: String?)
```

## Parameters

- `URLTemplate` — A string that you can use to build a URL to access your tile images. The string you specify can point to a local file or to an image on a remote server. To facilitate retrieving multiple tiles using the string, use the placeholder values `{x}`, `{y}`, `{z}`, and `{scale}` as stand-ins for the x and y tile indexes, the zoom level, and the resolution of the tile image. If this parameter is `nil`, you need to provide custom implementations for the tile-loading methods of this class.

## Return Value

An initialized tile overlay object.

## Discussion

The default tile overlay object uses the template string you specify to request tiles. This template string needs to incorporate the `{x}`, `{y}`, `{z}`, and `{scale}` placeholder strings to facilitate the creation of a URL for requesting the appropriate tile. For example, if you have a server that vends tiles when you provide a URL in the form of `http://myserver/tile?x=0&y=0&z=0&scale=1.0`, you specify a template string of `http://myserver/tile?x={x}&y={y}&z={z}&scale={scale}`. The tile overlay object substitutes actual index values for your template’s placeholders before requesting the tile.

## See Also

### Related Documentation

- [- URLForTilePath:](<url(fortilepath_).md>) — Returns the URL to use to access the specified tile.
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
