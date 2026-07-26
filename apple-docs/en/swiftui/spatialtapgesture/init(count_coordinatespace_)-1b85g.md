---
title: 'init(count:coordinateSpace:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 9.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)-1b85g'
source_url: 'https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)-1b85g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialtapgesture/init%28count%3Acoordinatespace%3A%29-1b85g.json'
content_hash: 'sha256:282e31e2dd3d4cd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SpatialTapGesture](../spatialtapgesture.md)

# init(count:coordinateSpace:)

<sub>Initializer</sub>

Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

> [!warning] Deprecated
> Use [init(count:coordinateSpace:)](<init(count_coordinatespace_)-75s7q.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(count: Int = 1, coordinateSpace: CoordinateSpace = .local)
```

## Parameters

- `count` — The required number of taps to complete the tap gesture.

- `coordinateSpace` — The coordinate space of the tap gesture’s location.
