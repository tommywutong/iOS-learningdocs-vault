---
title: 'bordered(alternatesRowBackgrounds:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 12.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/tablestyle/bordered(alternatesrowbackgrounds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablestyle/bordered(alternatesrowbackgrounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablestyle/bordered%28alternatesrowbackgrounds%3A%29.json'
content_hash: 'sha256:6b9b07c1b702f780'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableStyle](../tablestyle.md)

# bordered(alternatesRowBackgrounds:)

<sub>Type Method</sub>

The table style that describes the behavior and appearance of a table with standard border.

> [!warning] Deprecated
> Use the [bordered](bordered.md) style and add the [alternatingRowBackgrounds(_:)](<../view/alternatingrowbackgrounds(__).md>) view modifier instead.

<sub>macOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle
```

## Parameters

- `alternatesRowBackgrounds` — Whether the rows should alternate their backgrounds to help visually distinguish them from each other.

## Discussion

Bordered tables are expected to be inset from their outer containers, but do not have inset style rows or selection.

## See Also

### Deprecated styles

- [inset(alternatesRowBackgrounds:)](<inset(alternatesrowbackgrounds_).md>) — The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges. _(deprecated)_
