---
title: 'scrollEdgeEffectHidden(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrolledgeeffecthidden(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrolledgeeffecthidden(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrolledgeeffecthidden%28_%3Afor%3A%29.json'
content_hash: 'sha256:53b9fc2c2681c962'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollEdgeEffectHidden(_:for:)

<sub>Instance Method</sub>

Hides any scroll edge effects for scroll views within this hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
nonisolated func scrollEdgeEffectHidden(_ hidden: Bool = true, for edges: Edge.Set = .all) -> some View

```

## Discussion

By default, a scroll view renders an automatic edge effect style. Use this modifier to hide any edge effects for scroll views within this hierarchy.

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectHidden()
```

## See Also

### Configuring scroll edge effects

- [scrollEdgeEffectStyle(_:for:)](<scrolledgeeffectstyle(__for_).md>) — Configures the scroll edge effect style for scroll views within this hierarchy.
- [ScrollEdgeEffectStyle](../scrolledgeeffectstyle.md) — A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.
- [safeAreaBar(edge:alignment:spacing:content:)](<safeareabar(edge_alignment_spacing_content_).md>) — Shows the specified content as a custom bar beside the modified view.
