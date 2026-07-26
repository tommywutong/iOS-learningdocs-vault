---
title: 'init(count:coordinateSpace3D:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spatialtapgesture/init(count:coordinatespace3d:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace3d:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialtapgesture/init%28count%3Acoordinatespace3d%3A%29.json'
content_hash: 'sha256:0abd12be83b377cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SpatialTapGesture](../spatialtapgesture.md)

# init(count:coordinateSpace3D:)

<sub>Initializer</sub>

Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

<sub>visionOS</sub>

```swift
nonisolated init(count: Int = 1, coordinateSpace3D: some CoordinateSpace3D)
```

## Parameters

- `count` — The required number of taps to complete the tap gesture.

- `coordinateSpace3D` — The coordinate space 3D of the tap gesture’s location.

## See Also

### Creating a spatial tap gesture

- [init(count:coordinateSpace:)](<init(count_coordinatespace_)-75s7q.md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](<init(count_coordinatespace_).md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:inputKinds:)](<init(count_coordinatespace_inputkinds_).md>) — Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes. _(beta)_
- [coordinateSpace](coordinatespace.md) — The coordinate space in which to receive location values.
- [count](count.md) — The required number of tap events.
