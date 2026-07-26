---
title: 'contentMarginsRemoved(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/toolbarcontent/contentmarginsremoved(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcontent/contentmarginsremoved(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcontent/contentmarginsremoved%28_%3A%29.json'
content_hash: 'sha256:343df6b395819c65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarContent](../toolbarcontent.md)

# contentMarginsRemoved(_:)

<sub>Instance Method</sub>

Configures whether the content margins are removed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func contentMarginsRemoved(_ removed: Bool = true) -> some ToolbarContent

```

## Parameters

- `removed` — Whether the content margins should be removed.

## Discussion

Use this modifier to remove the default padding around a toolbar item’s content. This is useful for content that goes to the edge of the item.

```swift
.toolbar {
    ToolbarItem {
        CustomButton()
    }
    .contentMarginsRemoved()
}
```
