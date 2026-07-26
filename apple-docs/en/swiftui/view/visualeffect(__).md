---
title: 'visualEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/visualeffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/visualeffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/visualeffect%28_%3A%29.json'
content_hash: 'sha256:9e76150793e78c85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# visualEffect(_:)

<sub>Instance Method</sub>

Applies effects to this view, while providing access to layout information through a geometry proxy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func visualEffect(_ effect: @escaping @Sendable (EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View

```

## Parameters

- `effect` — A closure that returns the effect to be applied. The first argument provided to the closure is a placeholder representing this view. The second argument is a `GeometryProxy`.

## Return Value

A view with the effect applied.

## Discussion

You return new effects by calling functions on the first argument provided to the `effect` closure. In this example, `ContentView` is offset by its own size, causing its top left corner to appear where the bottom right corner was originally located:

```swift
ContentView()
    .visualEffect { content, geometryProxy in
        content.offset(geometryProxy.size)
    }
```

## See Also

### Applying effects based on geometry

- [visualEffect3D(_:)](<visualeffect3d(__).md>) — Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [VisualEffect](../visualeffect.md) — Visual Effects change the visual appearance of a view without changing its ancestors or descendents.
- [EmptyVisualEffect](../emptyvisualeffect.md) — The base visual effect that you apply additional effect to.
