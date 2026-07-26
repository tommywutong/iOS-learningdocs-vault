---
title: 'onInteractiveResizeChange(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oninteractiveresizechange(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oninteractiveresizechange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oninteractiveresizechange%28_%3A%29.json'
content_hash: 'sha256:a90eef7833e198d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onInteractiveResizeChange(_:)

<sub>Instance Method</sub>

Adds an action to perform when the enclosing window is being interactively resized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onInteractiveResizeChange(_ action: @escaping (Bool) -> Void) -> some View

```

## Parameters

- `action` — A closure to run when the state of the window’s interactive resize changes.

## Discussion

Use this modifier to adjust how your view behaves when a window is in the process of being resized by the user. The action provided to this modifier will be called when the resize action begins and ends.

For example, you can adjust the frame rate of a custom Metal renderer during interactive resize:

```swift
struct RootView: View {
    var renderer: MetalRenderer
    var body: some View {
        MetalRepresentable(renderer: renderer)
           .onInteractiveResizeChange { isResizing in
               // Let the renderer know the window is being actively
               // resized, so that it can adjust frame rate,
               // pause animations, etc.
               renderer.handleWindowResize(isResizing: isResizing)
           }
    }
}
```

## See Also

### Geometry

- [onGeometryChange(for:of:action:)](<ongeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a geometry proxy, changes.
- [onGeometryChange3D(for:of:action:)](<ongeometrychange3d(for_of_action_).md>) — Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
