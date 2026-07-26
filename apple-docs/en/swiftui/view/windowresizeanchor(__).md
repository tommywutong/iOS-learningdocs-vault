---
title: 'windowResizeAnchor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/windowresizeanchor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/windowresizeanchor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/windowresizeanchor%28_%3A%29.json'
content_hash: 'sha256:c9a2b09fe2416518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# windowResizeAnchor(_:)

<sub>Instance Method</sub>

Sets the window anchor point used when the size of the view changes such that the window must resize.

<sub>macOS</sub>

```swift
nonisolated func windowResizeAnchor(_ anchor: UnitPoint?) -> some View

```

## Parameters

- `anchor` — The window point fixed under programmatic size changes caused by the content size of the window changing. Defaults to a system defined value when `nil`.

## Return Value

A view whose scene resizes on `anchor`.

## Discussion

In SwiftUI life cycle apps, this modifier can be used to control how a window anchors when animating: drive window animations by changing the size of a view in a way that causes the window size to change. Note that if the window size is decreasing and an animation is desired, it is often necessary to (temporarily, if desired) set the [windowResizability(_:)](<../scene/windowresizability(__).md>) to [contentSize](../windowresizability/contentsize.md).

```swift
struct Scratchpad: App {
    var body: some Scene {
        WindowGroup {
            HeightResizingExample()
        }
        .windowResizability(.contentSize)
    }
}

struct HeightResizingExample: View {
    @State private var height: CGFloat = 300

    var body: some View {
        ZStack(alignment: .topLeading) {
            Color.red
                .overlay {
                    Text("Tap to toggle")
                        .foregroundStyle(.white)
                }
        }
        .onTapGesture {
            withAnimation(.easeInOut) {
                height = height == 300 ? 700 : 300
            }
        }
        .frame(width: 250, height: height)
        .windowResizeAnchor(.top)
    }
}
```

The default anchor varies by scene type and is used when `anchor` is nil. Generally, it resolves to the `.topLeading` corner.

> [!note] Note
> Animated window resizes are only supported in SwiftUI app-lifecycle apps. However, the anchor point is respected in all cases.

> [!note] Note
> When animating windows on macOS, it can be helpful to explicitly specify `.topLeading` to avoid pixel cracking between the hosting view and the hosting window.

## See Also

### Window behaviors

- [windowDismissBehavior(_:)](<windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowToolbarFullScreenVisibility(_:)](<windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [windowMinimizeBehavior(_:)](<windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowResizeBehavior(_:)](<windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
- [preferredWindowClippingMargins(_:_:)](<preferredwindowclippingmargins(____).md>) — Requests additional margins for drawing beyond the bounds of the window.
