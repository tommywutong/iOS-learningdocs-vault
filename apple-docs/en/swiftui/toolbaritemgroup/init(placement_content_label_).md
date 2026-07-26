---
title: 'init(placement:content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toolbaritemgroup/init(placement:content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemgroup/init(placement:content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemgroup/init%28placement%3Acontent%3Alabel%3A%29.json'
content_hash: 'sha256:8f2bf353ee00c895'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemGroup](../toolbaritemgroup.md)

# init(placement:content:label:)

<sub>Initializer</sub>

Creates a toolbar item group with the specified placement, content, and a label describing that content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<C, L>(placement: ToolbarItemPlacement = .automatic, @ContentBuilder content: () -> C, @ContentBuilder label: () -> L) where Content == LabeledToolbarItemGroupContent<C, L>, C : View, L : View
```

## Parameters

- `placement` — Which section of the toolbar the item should be placed in.

- `content` — The content of the item.

- `label` — The label describing the content of the item.

## Discussion

A toolbar item group provided a label wraps its content within a [ControlGroup](../controlgroup.md) which allows the content to collapse down into a menu that presents its content based on available space.

## See Also

### Creating a toolbar item group

- [init(placement:content:)](<init(placement_content_).md>) — Creates a toolbar item group with a specified placement and content.
