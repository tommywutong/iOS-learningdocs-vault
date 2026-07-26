---
title: 'spatialOverlay(alignment:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/spatialoverlay(alignment:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/spatialoverlay(alignment:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/spatialoverlay%28alignment%3Acontent%3A%29.json'
content_hash: 'sha256:6a55f81d900fc5f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# spatialOverlay(alignment:content:)

<sub>Instance Method</sub>

Adds secondary views within the 3D bounds of this view.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func spatialOverlay<V>(alignment: Alignment3D = .center, @ContentBuilder content: () -> V) -> some View where V : View

```

## Parameters

- `alignment` — The alignment with a default value of [center](../alignment3d/center.md) that you use to position the secondary view.

- `content` — The content builder which produces views to occupy the same 3D space as this view. Multiple views provided by content are organized into a [SpatialContainer](../spatialcontainer.md).

## Return Value

A view that adds `content` within the view’s 3D bounds.

## Discussion

Multiple views provided by `content` are stacked depthwise.

## See Also

### Foreground elements

- [border(_:width:)](<border(__width_).md>) — Adds a border to this view with the specified style and width.
- [overlay(alignment:content:)](<overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [spatialOverlayPreferenceValue(_:alignment:_:)](<spatialoverlaypreferencevalue(__alignment___).md>) — Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.
