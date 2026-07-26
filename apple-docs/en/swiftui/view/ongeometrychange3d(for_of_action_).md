---
title: 'onGeometryChange3D(for:of:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ongeometrychange3d(for:of:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ongeometrychange3d(for:of:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ongeometrychange3d%28for%3Aof%3Aaction%3A%29.json'
content_hash: 'sha256:899be251b19b7c85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onGeometryChange3D(for:of:action:)

<sub>Instance Method</sub>

Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func onGeometryChange3D<T>(for type: T.Type, of transform: @escaping (GeometryProxy3D) -> T, action: @escaping (T) -> Void) -> some View where T : Equatable

```

## See Also

### Geometry

- [onGeometryChange(for:of:action:)](<ongeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a geometry proxy, changes.
- [onInteractiveResizeChange(_:)](<oninteractiveresizechange(__).md>) — Adds an action to perform when the enclosing window is being interactively resized.
