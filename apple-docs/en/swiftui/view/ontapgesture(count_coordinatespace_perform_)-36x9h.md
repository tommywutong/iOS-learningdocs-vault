---
title: 'onTapGesture(count:coordinateSpace:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 9.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)-36x9h'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:)-36x9h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ontapgesture%28count%3Acoordinatespace%3Aperform%3A%29-36x9h.json'
content_hash: 'sha256:6c628249bb8ed5cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onTapGesture(count:coordinateSpace:perform:)

<sub>Instance Method</sub>

Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.

> [!warning] Deprecated
> Use [onTapGesture(count:coordinateSpace:perform:)](<ontapgesture(count_coordinatespace_perform_)-21n4i.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func onTapGesture(count: Int = 1, coordinateSpace: CoordinateSpace = .local, perform action: @escaping (CGPoint) -> Void) -> some View

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
