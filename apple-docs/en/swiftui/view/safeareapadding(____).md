---
title: 'safeAreaPadding(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/safeareapadding(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/safeareapadding(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/safeareapadding%28_%3A_%3A%29.json'
content_hash: 'sha256:1a9ed2936ffadbba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# safeAreaPadding(_:_:)

<sub>Instance Method</sub>

Adds the provided insets into the safe area of this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func safeAreaPadding(_ edges: Edge.Set = .all, _ length: CGFloat? = nil) -> some View

```

## Discussion

Use this modifier when you would like to add a fixed amount of space to the safe area a view sees.

```swift
ScrollView(.horizontal) {
    HStack(spacing: 10.0) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
}
.safeAreaPadding(.horizontal, 20.0)
```

See the horizontal [safeAreaInset(edge:alignment:spacing:content:)](<safeareainset(edge_alignment_spacing_content_)-6gwby.md>) or vertical [safeAreaInset(edge:alignment:spacing:content:)](<safeareainset(edge_alignment_spacing_content_)-4s51l.md>) modifier for adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

- [ignoresSafeArea(_:edges:)](<ignoressafearea(__edges_).md>) — Expands the safe area of a view.
- [ignoresSafeArea(_:edges:alignment:)](<ignoressafearea(__edges_alignment_).md>) — Expands the safe area of a view aligning content within the new bounds using the provided alignment. _(beta)_
- [safeAreaInset(edge:alignment:spacing:content:)](<safeareainset(edge_alignment_spacing_content_).md>) — Shows the specified content beside the modified view.
- [safeAreaPadding(_:)](<safeareapadding(__).md>) — Adds the provided insets into the safe area of this view.
- [SafeAreaRegions](../safearearegions.md) — A set of symbolic safe area regions.
