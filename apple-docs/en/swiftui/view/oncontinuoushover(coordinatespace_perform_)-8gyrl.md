---
title: 'onContinuousHover(coordinateSpace:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 13.0+（27.0 起废弃）, tvOS 16.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)-8gyrl'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oncontinuoushover(coordinatespace:perform:)-8gyrl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oncontinuoushover%28coordinatespace%3Aperform%3A%29-8gyrl.json'
content_hash: 'sha256:f4f004e508957042'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onContinuousHover(coordinateSpace:perform:)

<sub>Instance Method</sub>

Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.

> [!warning] Deprecated
> Use [onContinuousHover(coordinateSpace:perform:)](<oncontinuoushover(coordinatespace_perform_)-4ehfq.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func onContinuousHover(coordinateSpace: CoordinateSpace = .local, perform action: @escaping (HoverPhase) -> Void) -> some View

```

## Parameters

- `coordinateSpace` — The coordinate space for the location values. Defaults to [CoordinateSpace.local](../coordinatespace/local.md).

- `action` — The action to perform whenever the pointer enters, moves within, or exits the view’s bounds. The `action` closure passes the [HoverPhase.active(_:)](<../hoverphase/active(__).md>) phase with the pointer’s coordinates if the pointer is in the view’s bounds; otherwise, it passes [HoverPhase.ended](../hoverphase/ended.md).

## Return Value

A view that calls `action` when the pointer enters, moves within, or exits the view’s bounds.

## Discussion

Call this method to define a region for detecting pointer movement with the size and position of this view. The following example updates `hoverLocation` and `isHovering` to be based on the phase provided to the closure:

```swift
@State private var hoverLocation: CGPoint = .zero
@State private var isHovering = false

var body: some View {
    VStack {
        Color.red
            .frame(width: 400, height: 400)
            .onContinuousHover { phase in
                switch phase {
                case .active(let location):
                    hoverLocation = location
                    isHovering = true
                case .ended:
                    isHovering = false
                }
            }
            .overlay {
                Rectangle()
                    .frame(width: 50, height: 50)
                    .foregroundColor(isHovering ? .green : .blue)
                    .offset(x: hoverLocation.x, y: hoverLocation.y)
            }
    }
}
```
