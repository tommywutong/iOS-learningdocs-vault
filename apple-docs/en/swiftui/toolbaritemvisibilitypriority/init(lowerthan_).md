---
title: 'init(lowerThan:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/toolbaritemvisibilitypriority/init(lowerthan:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/init(lowerthan:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemvisibilitypriority/init%28lowerthan%3A%29.json'
content_hash: 'sha256:bf61e9cbbe816b59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemVisibilityPriority](../toolbaritemvisibilitypriority.md)

# init(lowerThan:)

<sub>Initializer</sub>

Creates a priority lower than the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(lowerThan other: ToolbarItemVisibilityPriority)
```

## Discussion

The priority is lower than `other` but doesn’t cross below the next lower system priority. For example, `ToolbarItemVisibilityPriority(lowerThan: .high)` returns a value that is less than `.high` but greater than `.automatic`.

Priorities created with the same base value are equal:

```swift
let x = ToolbarItemVisibilityPriority(lowerThan: .high)
let y = ToolbarItemVisibilityPriority(lowerThan: .high)
x == y // true
```

## See Also

### Creating custom priorities

- [init(higherThan:)](<init(higherthan_).md>) — Creates a priority higher than the specified value. _(beta)_
