---
title: low
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemvisibilitypriority/low
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/low'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemvisibilitypriority/low.json'
content_hash: 'sha256:ad95a3d015b53e18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemVisibilityPriority](../toolbaritemvisibilitypriority.md)

# low

<sub>Type Property</sub>

A priority that moves the item to the overflow menu before items with the default or high priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
static let low: ToolbarItemVisibilityPriority
```

## Discussion

Use for secondary actions, such as archive or delete, that don’t need persistent visibility in the toolbar.

## See Also

### Getting system priorities

- [automatic](automatic.md) — The default priority that lets the system determine the item’s visibility in the toolbar.
- [high](high.md) — A priority that keeps the item in the toolbar longer than items with the default or low priority.
