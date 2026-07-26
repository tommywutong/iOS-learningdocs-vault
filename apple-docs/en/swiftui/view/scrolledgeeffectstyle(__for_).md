---
title: 'scrollEdgeEffectStyle(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrolledgeeffectstyle(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrolledgeeffectstyle(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrolledgeeffectstyle%28_%3Afor%3A%29.json'
content_hash: 'sha256:07fa0209f1f268a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollEdgeEffectStyle(_:for:)

<sub>Instance Method</sub>

Configures the scroll edge effect style for scroll views within this hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
nonisolated func scrollEdgeEffectStyle(_ style: ScrollEdgeEffectStyle?, for edges: Edge.Set) -> some View

```

## Discussion

By default, a scroll view renders an automatic edge effect. Use this modifier to change the scroll edge effect style.

```swift
ScrollView {
    LazyVStack {
        ForEach(data) { item in
            RowView(item)
        }
    }
}
.scrollEdgeEffectStyle(.hard, for: .all)
```

## See Also

### Configuring scroll edge effects

- [scrollEdgeEffectHidden(_:for:)](<scrolledgeeffecthidden(__for_).md>) — Hides any scroll edge effects for scroll views within this hierarchy.
- [ScrollEdgeEffectStyle](../scrolledgeeffectstyle.md) — A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.
- [safeAreaBar(edge:alignment:spacing:content:)](<safeareabar(edge_alignment_spacing_content_).md>) — Shows the specified content as a custom bar beside the modified view.
