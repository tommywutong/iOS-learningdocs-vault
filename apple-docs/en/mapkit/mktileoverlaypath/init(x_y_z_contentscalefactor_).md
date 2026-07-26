---
title: 'init(x:y:z:contentScaleFactor:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mktileoverlaypath/init(x:y:z:contentscalefactor:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mktileoverlaypath/init(x:y:z:contentscalefactor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mktileoverlaypath/init%28x%3Ay%3Az%3Acontentscalefactor%3A%29.json'
content_hash: 'sha256:57772471fdfb7e06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKTileOverlayPath](../mktileoverlaypath.md)

# init(x:y:z:contentScaleFactor:)

<sub>Initializer</sub>

Creates a new overlay path with the specified indexes and content scale factor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(x: Int, y: Int, z: Int, contentScaleFactor: CGFloat)
```

## Parameters

- `x` — The index of the tile along the x-axis of the map.

- `y` — The index of the tile along the y-axis of the map.

- `z` — The index of the tile along the z-axis of the map.

- `contentScaleFactor` — The screen scale that the framework shows the tile. This value is typically either `1.0` (for standard resolution displays) or `2.0` (for Retina displays).

## See Also

### Creating a tile overlay path

- [init()](<init().md>) — Creates a new tile overlay path.
