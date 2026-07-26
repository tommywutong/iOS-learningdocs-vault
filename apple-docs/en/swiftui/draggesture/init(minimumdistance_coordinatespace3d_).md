---
title: 'init(minimumDistance:coordinateSpace3D:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace3d:)'
source_url: 'https://developer.apple.com/documentation/swiftui/draggesture/init(minimumdistance:coordinatespace3d:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/draggesture/init%28minimumdistance%3Acoordinatespace3d%3A%29.json'
content_hash: 'sha256:7dc4a20d4b7e0851'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragGesture](../draggesture.md)

# init(minimumDistance:coordinateSpace3D:)

<sub>Initializer</sub>

Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency init(minimumDistance: CGFloat = 0, coordinateSpace3D: some CoordinateSpace3D)
```

## Parameters

- `minimumDistance` — The minimum dragging distance for the gesture to succeed. Ensure this unit is in the same scale as the provided `CoordinateSpace3D`, the default value is 0 to avoid issues around differing coordinate space scales.

- `coordinateSpace3D` — The coordinate space 3D of the dragging gesture’s location.

## See Also

### Creating a drag gesture

- [init(minimumDistance:coordinateSpace:)](<init(minimumdistance_coordinatespace_)-8ffe5.md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:)](<init(minimumdistance_coordinatespace_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [init(minimumDistance:coordinateSpace:inputKinds:)](<init(minimumdistance_coordinatespace_inputkinds_).md>) — Creates a dragging gesture with the minimum dragging distance before the gesture succeeds, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes. _(beta)_
- [minimumDistance](minimumdistance.md) — The minimum dragging distance before the gesture succeeds.
- [coordinateSpace](coordinatespace.md) — The coordinate space in which to receive location values.
