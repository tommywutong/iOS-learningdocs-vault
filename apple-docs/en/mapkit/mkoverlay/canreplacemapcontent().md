---
title: canReplaceMapContent()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkoverlay/canreplacemapcontent()
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlay/canreplacemapcontent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlay/canreplacemapcontent%28%29.json'
content_hash: 'sha256:f228c247d9e64a52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlay](../mkoverlay.md)

# canReplaceMapContent()

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the overlay content replaces the underlying map content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func canReplaceMapContent() -> Bool
```

## Return Value

[true](../../swift/true.md) if the map view can skip the loading and drawing of the underlying map tiles, or [false](../../swift/false.md) if the map view needs to draw the tiles.

## Discussion

The map view uses the return value of this method as a hint to determine whether it loads and renders its tiles. If your overlay covers its designated region entirely with opaque content, and effectively replaces the content of underlying map tiles, implement this method and return [true](../../swift/true.md). Doing so alleviates the need for the map to render its tiles.

If you don’t implement this method, or if you return [false](../../swift/false.md) from it, the map view continues to load and render its tiles.
