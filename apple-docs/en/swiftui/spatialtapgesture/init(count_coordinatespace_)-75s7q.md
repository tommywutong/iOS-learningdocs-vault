---
title: 'init(count:coordinateSpace:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)-75s7q'
source_url: 'https://developer.apple.com/documentation/swiftui/spatialtapgesture/init(count:coordinatespace:)-75s7q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialtapgesture/init%28count%3Acoordinatespace%3A%29-75s7q.json'
content_hash: 'sha256:40ebc79602d17b9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SpatialTapGesture](../spatialtapgesture.md)

# init(count:coordinateSpace:)

<sub>Initializer</sub>

Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local)
```

## Parameters

- `count` — The required number of taps to complete the tap gesture.

- `coordinateSpace` — The coordinate space of the tap gesture’s location.

## See Also

### Creating a spatial tap gesture

- [init(count:coordinateSpace:)](<init(count_coordinatespace_).md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace3D:)](<init(count_coordinatespace3d_).md>) — Creates a tap gesture with the number of required taps and the coordinate space of the gesture’s location.
- [init(count:coordinateSpace:inputKinds:)](<init(count_coordinatespace_inputkinds_).md>) — Creates a tap gesture with the number of required taps, the coordinate space of the gesture’s location, and the input kinds the gesture recognizes. _(beta)_
- [coordinateSpace](coordinatespace.md) — The coordinate space in which to receive location values.
- [count](count.md) — The required number of tap events.
