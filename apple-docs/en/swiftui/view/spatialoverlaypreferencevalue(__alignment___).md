---
title: 'spatialOverlayPreferenceValue(_:alignment:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/spatialoverlaypreferencevalue(_:alignment:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/spatialoverlaypreferencevalue(_:alignment:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/spatialoverlaypreferencevalue%28_%3Aalignment%3A_%3A%29.json'
content_hash: 'sha256:72028e95eac0ecd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# spatialOverlayPreferenceValue(_:alignment:_:)

<sub>Instance Method</sub>

Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func spatialOverlayPreferenceValue<K, V>(_ key: K.Type, alignment: Alignment3D = .center, @ContentBuilder _ transform: @escaping (K.Value) -> V) -> some View where K : PreferenceKey, V : View

```

## See Also

### Foreground elements

- [border(_:width:)](<border(__width_).md>) — Adds a border to this view with the specified style and width.
- [overlay(alignment:content:)](<overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [spatialOverlay(alignment:content:)](<spatialoverlay(alignment_content_).md>) — Adds secondary views within the 3D bounds of this view.
