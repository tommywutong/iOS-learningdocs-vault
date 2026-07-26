---
title: 'init(higherThan:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/toolbaritemvisibilitypriority/init(higherthan:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/init(higherthan:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemvisibilitypriority/init%28higherthan%3A%29.json'
content_hash: 'sha256:ca21a1997c25ef57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemVisibilityPriority](../toolbaritemvisibilitypriority.md)

# init(higherThan:)

<sub>Initializer</sub>

Creates a priority higher than the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(higherThan other: ToolbarItemVisibilityPriority)
```

## Discussion

The priority is higher than `other` but doesn’t cross above the next higher system priority. For example, `ToolbarItemVisibilityPriority(higherThan: .high)` returns a value that is greater than `.high`.

Priorities created with the same base value are equal:

```swift
let x = ToolbarItemVisibilityPriority(higherThan: .high)
let y = ToolbarItemVisibilityPriority(higherThan: .high)
x == y // true
```

## See Also

### Creating custom priorities

- [init(lowerThan:)](<init(lowerthan_).md>) — Creates a priority lower than the specified value. _(beta)_
