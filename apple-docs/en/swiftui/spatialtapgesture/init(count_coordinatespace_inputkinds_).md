---
title: 'init(count:coordinateSpace:inputKinds:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:inputkinds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:inputkinds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialtapgesture/init%28count%3Acoordinatespace%3Ainputkinds%3A%29.json'
content_hash: 'sha256:518c3d48f4a89032'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SpatialTapGesture](../spatialtapgesture.md)

# init(count:coordinateSpace:inputKinds:)

<sub>Initializer</sub>

Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `count` — The required number of taps to complete the tap gesture.

- `coordinateSpace` — The coordinate space of the tap gesture’s location.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating a spatial tap gesture

- [init(count:coordinateSpace:)](<init(count_coordinatespace_)-75s7q.md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:)](<init(count_coordinatespace_).md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace3D:)](<init(count_coordinatespace3d_).md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [coordinateSpace](coordinatespace.md) — The coordinate space in which to receive location values.
- [count](count.md) — The required number of tap events.
