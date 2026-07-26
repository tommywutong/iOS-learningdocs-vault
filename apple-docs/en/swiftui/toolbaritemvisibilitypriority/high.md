---
title: high
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemvisibilitypriority/high
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/high'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemvisibilitypriority/high.json'
content_hash: 'sha256:7de0179d8b1b2310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemVisibilityPriority](../toolbaritemvisibilitypriority.md)

# high

<sub>Type Property</sub>

A priority that keeps the item in the toolbar longer than items with the default or low priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static let high: ToolbarItemVisibilityPriority
```

## Discussion

Use for frequently used actions that need to stay visible as the toolbar shrinks.

## See Also

### Getting system priorities

- [automatic](automatic.md) — The default priority that lets the system determine the item’s visibility in the toolbar.
- [low](low.md) — A priority that moves the item to the overflow menu before items with the default or high priority.
