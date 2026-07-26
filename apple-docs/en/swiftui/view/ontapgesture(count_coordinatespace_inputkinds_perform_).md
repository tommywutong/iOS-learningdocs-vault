---
title: 'onTapGesture(count:coordinateSpace:inputKinds:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/ontapgesture(count:coordinatespace:inputkinds:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:inputkinds:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ontapgesture%28count%3Acoordinatespace%3Ainputkinds%3Aperform%3A%29.json'
content_hash: 'sha256:050346f64116f9c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onTapGesture(count:coordinateSpace:inputKinds:perform:)

<sub>Instance Method</sub>

Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onTapGesture(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local, inputKinds: GestureInputKinds = .all, perform action: @escaping (CGPoint) -> Void) -> some View

```

## Parameters

- `count` — The number of taps or clicks required to trigger the action closure provided in `action`.

- `coordinateSpace` — The coordinate space in which to receive location values.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

- `action` — The action to perform. This closure receives an input that indicates where the interaction occurred.

## See Also

### Recognizing tap gestures

- [onTapGesture(count:perform:)](<ontapgesture(count_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:perform:)](<ontapgesture(count_coordinatespace_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [TapGesture](../tapgesture.md) — A gesture that recognizes one or more taps.
- [SpatialTapGesture](../spatialtapgesture.md) — A gesture that recognizes one or more taps and reports their location.
