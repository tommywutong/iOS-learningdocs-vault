---
title: 'onTapGesture(count:coordinateSpace:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ontapgesture%28count%3Acoordinatespace%3Aperform%3A%29.json'
content_hash: 'sha256:eedc345d7e2b4b97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onTapGesture(count:coordinateSpace:perform:)

<sub>Instance Method</sub>

Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func onTapGesture(count: Int = 1, coordinateSpace: some CoordinateSpaceProtocol = .local, perform action: @escaping (CGPoint) -> Void) -> some View

```

## Parameters

- `count` — The number of taps or clicks required to trigger the action closure provided in `action`. Defaults to `1`.

- `coordinateSpace` — The coordinate space in which to receive location values. Defaults to [CoordinateSpace.local](../coordinatespace/local.md).

- `action` — The action to perform. This closure receives an input that indicates where the interaction occurred.

## Discussion

Use this method to perform the specified `action` when the user clicks or taps on the modified view `count` times. The action closure receives the location of the interaction.

> [!note] Note
> If you create a control that’s functionally equivalent to a [Button](../button.md), use [ButtonStyle](../buttonstyle.md) to create a customized button instead.

The following code adds a tap gesture to a [Circle](../circle.md) that toggles the color of the circle based on the tap location.

```swift
struct TapGestureExample: View {
    @State private var location: CGPoint = .zero

    var body: some View {
        Circle()
            .fill(self.location.y > 50 ? Color.blue : Color.red)
            .frame(width: 100, height: 100, alignment: .center)
            .onTapGesture { location in
                self.location = location
            }
    }
}
```

## See Also

### Recognizing tap gestures

- [onTapGesture(count:perform:)](<ontapgesture(count_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:inputKinds:perform:)](<ontapgesture(count_coordinatespace_inputkinds_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(beta)_
- [TapGesture](../tapgesture.md) — A gesture that recognizes one or more taps.
- [SpatialTapGesture](../spatialtapgesture.md) — A gesture that recognizes one or more taps and reports their location.
