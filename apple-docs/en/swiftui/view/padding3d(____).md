---
title: 'padding3D(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/padding3d(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/padding3d(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/padding3d%28_%3A_%3A%29.json'
content_hash: 'sha256:b71d772372036b9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# padding3D(_:_:)

<sub>Instance Method</sub>

Pads this view using the edge insets you specify.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func padding3D(_ edges: Edge3D.Set = .all, _ length: CGFloat? = nil) -> some View

```

## Parameters

- `edges` — The set of edges along which to inset this view.

- `length` — The amount to inset this view on each edge. If `nil`, the amount is the system default amount.

## Return Value

A view that pads this view using edge the insets you specify.

## See Also

### Adding padding around a view

- [padding(_:)](<padding(__).md>) — Adds a different padding amount to each edge of this view.
- [padding(_:_:)](<padding(____).md>) — Adds an equal padding amount to specific edges of this view.
- [padding3D(_:)](<padding3d(__).md>) — Pads this view using the edge insets you specify.
- [scenePadding(_:)](<scenepadding(__).md>) — Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [scenePadding(_:edges:)](<scenepadding(__edges_).md>) — Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [ScenePadding](../scenepadding.md) — The padding used to space a view from its containing scene.
