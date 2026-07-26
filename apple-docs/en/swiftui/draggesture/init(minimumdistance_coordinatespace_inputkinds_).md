---
title: 'init(minimumDistance:coordinateSpace:inputKinds:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:inputkinds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:inputkinds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/init%28minimumdistance%3Acoordinatespace%3Ainputkinds%3A%29.json'
content_hash: 'sha256:61e7f04e90e6f1a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragGesture](../draggesture.md)

# init(minimumDistance:coordinateSpace:inputKinds:)

<sub>Initializer</sub>

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(minimumDistance: CGFloat = 10, coordinateSpace: some CoordinateSpaceProtocol = .local, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumDistance` — The minimum distance a person needs to drag before the drag gesture begins.

- `coordinateSpace` — The coordinate space of the dragging gesture’s location.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating a drag gesture

- [init(minimumDistance:coordinateSpace:)](<init(minimumdistance_coordinatespace_)-8ffe5.md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](<init(minimumdistance_coordinatespace_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace3D:)](<init(minimumdistance_coordinatespace3d_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [minimumDistance](minimumdistance.md) — The minimum dragging distance before the gesture succeeds.
- [coordinateSpace](coordinatespace.md) — The coordinate space in which to receive location values.
