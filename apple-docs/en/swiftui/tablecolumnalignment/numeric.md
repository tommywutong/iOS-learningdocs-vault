---
title: numeric
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumnalignment/numeric
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnalignment/numeric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnalignment/numeric.json'
content_hash: 'sha256:ed5536fac726c776'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnAlignment](../tablecolumnalignment.md)

# numeric

<sub>Type Property</sub>

Column alignment appropriate for numeric content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var numeric: TableColumnAlignment { get }
```

## Discussion

Use this alignment when a table column is primarily displaying numeric content, so that the values are easy to visually scan and compare.

This uses the current locale’s numbering system to determine the alignment:

- For left to right numbering systems, this is equivalent to right.
- For right to left numbering systems, this is equivalent to left.

## See Also

### Getting the alignment

- [automatic](automatic.md) — The default column alignment.
- [leading](leading.md) — Leading column alignment.
- [center](center.md) — Center column alignment.
- [trailing](trailing.md) — Trailing column alignment.
- [numeric(_:)](<numeric(__).md>) — Column alignment appropriate for numeric content.
