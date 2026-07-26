---
title: HStack
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hstack
source_url: 'https://developer.apple.com/documentation/swiftui/hstack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hstack.json'
content_hash: 'sha256:72681c22125a4be0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HStack

<sub>Structure</sub>

A view that arranges its subviews in a horizontal line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct HStack<Content> where Content : View
```

## Overview

Unlike [LazyHStack](lazyhstack.md), which only renders the views when your app needs to display them onscreen, an `HStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `HStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple horizontal stack of five text views:

```swift
var body: some View {
    HStack(
        alignment: .top,
        spacing: 10
    ) {
        ForEach(
            1...5,
            id: \.self
        ) {
            Text("Item \($0)")
        }
    }
}
```

![Five text views, named Item 1 through Item 5, arranged in a](../../../attachments/4d9bc52c0fbde5252c797d82d913a50b/SwiftUI-HStack-simple@2x.png)

> [!note] Note
> If you need a horizontal stack that conforms to the [Layout](layout.md) protocol, like when you want to create a conditional layout using [AnyLayout](anylayout.md), use [HStackLayout](hstacklayout.md) instead.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a stack

- [init(alignment:spacing:content:)](<hstack/init(alignment_spacing_content_).md>) — Creates a horizontal stack with the given spacing and vertical alignment.

## See Also

### Statically arranging views in one dimension

- [Building layouts with stack views](building-layouts-with-stack-views.md) — Compose complex layouts from primitive container views.
- [VStack](vstack.md) — A view that arranges its subviews in a vertical line.
