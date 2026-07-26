---
title: VStack
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/vstack
source_url: 'https://developer.apple.com/documentation/swiftui/vstack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/vstack.json'
content_hash: 'sha256:892920b0edcd36a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VStack

<sub>Structure</sub>

A view that arranges its subviews in a vertical line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct VStack<Content> where Content : View
```

## Overview

Unlike [LazyVStack](lazyvstack.md), which only renders the views when your app needs to display them, a `VStack` renders the views all at once, regardless of whether they are on- or offscreen. Use the regular `VStack` when you have a small number of subviews or don’t want the delayed rendering behavior of the “lazy” version.

The following example shows a simple vertical stack of 10 text views:

```swift
var body: some View {
    VStack(
        alignment: .leading,
        spacing: 10
    ) {
        ForEach(
            1...10,
            id: \.self
        ) {
            Text("Item \($0)")
        }
    }
}
```

![Ten text views, named Item 1 through Item 10, arranged in a](../../../attachments/93d31b000cb6f5419689a7b765474401/SwiftUI-VStack-simple@2x.png)

> [!note] Note
> If you need a vertical stack that conforms to the [Layout](layout.md) protocol, like when you want to create a conditional layout using [AnyLayout](anylayout.md), use [VStackLayout](vstacklayout.md) instead.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a stack

- [init(alignment:spacing:content:)](<vstack/init(alignment_spacing_content_).md>) — Creates an instance with the given spacing and horizontal alignment.

## See Also

### Statically arranging views in one dimension

- [Building layouts with stack views](building-layouts-with-stack-views.md) — Compose complex layouts from primitive container views.
- [HStack](hstack.md) — A view that arranges its subviews in a horizontal line.
