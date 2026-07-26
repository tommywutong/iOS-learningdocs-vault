---
title: 'contentMargins(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/contentmargins(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/contentmargins(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/contentmargins%28_%3Afor%3A%29.json'
content_hash: 'sha256:bf36684b28c26c68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# contentMargins(_:for:)

<sub>Instance Method</sub>

Configures the content margin for a provided placement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func contentMargins(_ length: CGFloat, for placement: ContentMarginPlacement = .automatic) -> some View

```

## Parameters

- `length` — The amount of margins to add on all edges.

- `placement` — Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of views. For example, you can use this modifier to customize the margins of scrollable views like [ScrollView](../scrollview.md). In the following example, the scroll view will automatically inset its content by the safe area plus an additional 20 points on the leading and trailing edge.

```swift
ScrollView(.horizontal) {
    // ...
}
.contentMargins(.horizontal, 20.0)
```

You can provide a [ContentMarginPlacement](../contentmarginplacement.md) to target specific parts of a view to customize. For example, provide a [scrollContent](../contentmarginplacement/scrollcontent.md) placement to inset the content of a [TextEditor](../texteditor.md) without affecting the insets of its scroll indicators.

```swift
TextEditor(text: $text)
    .contentMargins(.horizontal, 20.0, for: .scrollContent)
```

Similarly, you can customize the insets of scroll indicators separately from scroll content. Consider doing this when applying a custom clip shape that may clip the indicators.

```swift
ScrollView {
    // ...
}
.clipShape(.rect(cornerRadius: 20.0))
.contentMargins(10.0, for: .scrollIndicators)
```

When applying multiple contentMargins modifiers, modifiers with the same placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

- [contentMargins(_:_:for:)](<contentmargins(____for_).md>) — Configures the content margin for a provided placement.
- [ContentMarginPlacement](../contentmarginplacement.md) — The placement of margins.
