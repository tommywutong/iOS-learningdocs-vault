---
title: 'init(placement:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbaritemgroup/init(placement:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemgroup/init(placement:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemgroup/init%28placement%3Acontent%3A%29.json'
content_hash: 'sha256:22ffcd154440884c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemGroup](../toolbaritemgroup.md)

# init(placement:content:)

<sub>Initializer</sub>

Creates a toolbar item group with a specified placement and content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(placement: ToolbarItemPlacement = .automatic, @ContentBuilder content: () -> Content)
```

## Discussion

- placement: Which section of the toolbar all of its vended `ToolbarItem`s should be placed in.
- content: The content of the group. Each view specified in the `ContentBuilder` will be given its own `ToolbarItem` in the toolbar.

## See Also

### Creating a toolbar item group

- [init(placement:content:label:)](<init(placement_content_label_).md>) — Creates a toolbar item group with the specified placement, content, and a label describing that content.
