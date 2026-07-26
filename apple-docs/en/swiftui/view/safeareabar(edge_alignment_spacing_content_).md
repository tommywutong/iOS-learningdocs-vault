---
title: 'safeAreaBar(edge:alignment:spacing:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/safeareabar%28edge%3Aalignment%3Aspacing%3Acontent%3A%29.json'
content_hash: 'sha256:70ab4703332d2106'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# safeAreaBar(edge:alignment:spacing:content:)

<sub>Instance Method</sub>

Shows the specified content as a custom bar beside the modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ContentBuilder content: () -> some View) -> some View

```

## Parameters

- `edge` — The horizontal edge of the view on which `content` is placed.

- `alignment` — The alignment guide used to position `content` vertically.

- `spacing` — Extra distance placed between the two views, or nil to use the default amount of spacing.

- `content` — A content builder function providing the view to display as a custom bar.

## Return Value

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view, adjusting the safe area and scroll edge effects to match.

## Discussion

Similar to the [safeAreaInset(edge:alignment:spacing:content:)](<safeareainset(edge_alignment_spacing_content_)-6gwby.md>) modifier, the `content` view is anchored to the specified horizontal edge of the parent view and its width insets the safe area.

Additionally, it extends the edge effect of any scroll views affected by the inset safe area.

## See Also

### Configuring scroll edge effects

- [scrollEdgeEffectStyle(_:for:)](<scrolledgeeffectstyle(__for_).md>) — Configures the scroll edge effect style for scroll views within this hierarchy.
- [scrollEdgeEffectHidden(_:for:)](<scrolledgeeffecthidden(__for_).md>) — Hides any scroll edge effects for scroll views within this hierarchy.
- [ScrollEdgeEffectStyle](../scrolledgeeffectstyle.md) — A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.
