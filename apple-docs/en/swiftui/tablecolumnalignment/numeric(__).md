---
title: 'numeric(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumnalignment/numeric(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnalignment/numeric(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnalignment/numeric%28_%3A%29.json'
content_hash: 'sha256:5a4e0d20270c43c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnAlignment](../tablecolumnalignment.md)

# numeric(_:)

<sub>Type Method</sub>

Column alignment appropriate for numeric content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static func numeric(_ numberingSystem: Locale.NumberingSystem) -> TableColumnAlignment
```

## Discussion

Use this alignment when a table column is primarily displaying numeric content, so that the values are easy to visually scan and compare.

This uses the provided numbering system to determine the alignment:

- For left to right numbering systems, this is equivalent to right.
- For right to left numbering systems, this is equivalent to left.

## See Also

### Getting the alignment

- [automatic](automatic.md) — The default column alignment.
- [leading](leading.md) — Leading column alignment.
- [center](center.md) — Center column alignment.
- [trailing](trailing.md) — Trailing column alignment.
- [numeric](numeric.md) — Column alignment appropriate for numeric content.
