---
title: bordered
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablestyle/bordered
source_url: 'https://developer.apple.com/documentation/swiftui/tablestyle/bordered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablestyle/bordered.json'
content_hash: 'sha256:9c10b8b02523dd92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableStyle](../tablestyle.md)

# bordered

<sub>Type Property</sub>

The table style that describes the behavior and appearance of a table with standard border.

<sub>macOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var bordered: BorderedTableStyle { get }
```

## Discussion

Bordered tables are expected to be inset from their outer containers, but do not have inset style rows or selection.

To customize whether the rows of the table should alternate their backgrounds, use [alternatingRowBackgrounds(_:)](<../view/alternatingrowbackgrounds(__).md>).

## See Also

### Getting built-in table styles

- [automatic](automatic.md) — The default table style in the current context.
- [inset](inset.md) — The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
