---
title: LazyHStack
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/lazyhstack
source_url: 'https://developer.apple.com/documentation/swiftui/lazyhstack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/lazyhstack.json'
content_hash: 'sha256:0beaccb458ca6c10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LazyHStack

<sub>Structure</sub>

A view that arranges its children in a line that grows horizontally, creating items only as needed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct LazyHStack<Content> where Content : View
```

## Overview

The stack is “lazy,” in that the stack view doesn’t create items until it needs to render them onscreen.

In the following example, a [ScrollView](scrollview.md) contains a `LazyHStack` that consists of a horizontal row of text views. The stack aligns to the top of the scroll view and uses 10-point spacing between each text view.

```swift
ScrollView(.horizontal) {
    LazyHStack(alignment: .top, spacing: 10) {
        ForEach(1...100, id: \.self) {
            Text("Column \($0)")
        }
    }
}
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a lazy-loading horizontal stack

- [init(alignment:spacing:pinnedViews:content:)](<lazyhstack/init(alignment_spacing_pinnedviews_content_).md>) — Creates a lazy horizontal stack view with the given spacing, vertical alignment, pinning behavior, and content.

## See Also

### Dynamically arranging views in one dimension

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md) — Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md) — Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [LazyVStack](lazyvstack.md) — A view that arranges its children in a line that grows vertically, creating items only as needed.
- [PinnedScrollableViews](pinnedscrollableviews.md) — A set of view types that may be pinned to the bounds of a scroll view.
