---
title: 'visualEffect3D(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/visualeffect3d(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/visualeffect3d(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/visualeffect3d%28_%3A%29.json'
content_hash: 'sha256:7946e6c761a5ea76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# visualEffect3D(_:)

<sub>Instance Method</sub>

Applies effects to this view, while providing access to layout information through a 3D geometry proxy.

<sub>visionOS</sub>

```swift
nonisolated func visualEffect3D(_ effect: @escaping @Sendable (EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View

```

## Parameters

- `effect` — A closure that returns the effect to be applied. The first argument provided to the closure is a placeholder representing this view. The second argument is a `GeometryProxy3D`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to the `effect` closure. In this example, `ContentView` is offset in Z by its own depth, causing its back face to appear where the front face of the view was originally located:

```swift
ContentView()
    .visualEffect3D { content, geometryProxy in
        content.offset(z: geometryProxy.size.depth)
    }
```

## See Also

### Applying effects based on geometry

- [visualEffect(_:)](<visualeffect(__).md>) — Applies effects to this view, while providing access to layout information through a geometry proxy.
- [VisualEffect](../visualeffect.md) — Visual Effects change the visual appearance of a view without changing its ancestors or descendents.
- [EmptyVisualEffect](../emptyvisualeffect.md) — The base visual effect that you apply additional effect to.
