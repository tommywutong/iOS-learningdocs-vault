---
title: LazyVStack
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/lazyvstack
source_url: 'https://developer.apple.com/documentation/swiftui/lazyvstack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/lazyvstack.json'
content_hash: 'sha256:d4b266f9b40c7f35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LazyVStack

<sub>Structure</sub>

A view that arranges its children in a line that grows vertically, creating items only as needed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct LazyVStack<Content> where Content : View
```

## Overview

The stack is “lazy,” in that the stack view doesn’t create items until it needs to render them onscreen.

In the following example, a [ScrollView](scrollview.md) contains a `LazyVStack` that consists of a vertical row of text views. The stack aligns to the leading edge of the scroll view, and uses default spacing between the text views.

```swift
ScrollView {
    LazyVStack(alignment: .leading) {
        ForEach(1...100, id: \.self) {
            Text("Row \($0)")
        }
    }
}
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a lazy-loading vertical stack

- [init(alignment:spacing:pinnedViews:content:)](<lazyvstack/init(alignment_spacing_pinnedviews_content_).md>) — Creates a lazy vertical stack view with the given spacing, vertical alignment, pinning behavior, and content.

## See Also

### Dynamically arranging views in one dimension

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md) — Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md) — Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [LazyHStack](lazyhstack.md) — A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [PinnedScrollableViews](pinnedscrollableviews.md) — A set of view types that may be pinned to the bounds of a scroll view.
