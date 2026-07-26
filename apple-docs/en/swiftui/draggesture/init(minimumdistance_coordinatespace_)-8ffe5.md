---
title: 'init(minimumDistance:coordinateSpace:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-8ffe5'
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace:)-8ffe5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/init%28minimumdistance%3Acoordinatespace%3A%29-8ffe5.json'
content_hash: 'sha256:290168e6ec198ac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragGesture](../draggesture.md)

# init(minimumDistance:coordinateSpace:)

<sub>Initializer</sub>

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(minimumDistance: CGFloat = 10, coordinateSpace: some CoordinateSpaceProtocol = .local)
```

## Parameters

- `minimumDistance` — The minimum dragging distance for the gesture to succeed.

- `coordinateSpace` — The coordinate space of the dragging gesture’s location.

## See Also

### Creating a drag gesture

- [init(minimumDistance:coordinateSpace:)](<init(minimumdistance_coordinatespace_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace3D:)](<init(minimumdistance_coordinatespace3d_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:inputKinds:)](<init(minimumdistance_coordinatespace_inputkinds_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes. _(beta)_
- [minimumDistance](minimumdistance.md) — The minimum dragging distance before the gesture succeeds.
- [coordinateSpace](coordinatespace.md) — The coordinate space in which to receive location values.
