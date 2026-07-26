---
title: 'init(minimumDistance:coordinateSpace:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-3804h'
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-3804h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/init%28minimumdistance%3Acoordinatespace%3A%29-3804h.json'
content_hash: 'sha256:0fa465d660a4e7b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragGesture](../draggesture.md)

# init(minimumDistance:coordinateSpace:)

<sub>Initializer</sub>

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

> [!warning] Deprecated
> Use [init(minimumDistance:coordinateSpace:)](<init(minimumdistance_coordinatespace_)-8ffe5.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(minimumDistance: CGFloat = 10, coordinateSpace: CoordinateSpace = .local)
```

## Parameters

- `minimumDistance` — The minimum dragging distance for the gesture to succeed.

- `coordinateSpace` — The coordinate space of the dragging gesture’s location.
