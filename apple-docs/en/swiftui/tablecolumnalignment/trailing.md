---
title: trailing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tablecolumnalignment/trailing
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnalignment/trailing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnalignment/trailing.json'
content_hash: 'sha256:e308a824d6229a6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnAlignment](../tablecolumnalignment.md)

# trailing

<sub>Type Property</sub>

Trailing column alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var trailing: TableColumnAlignment { get }
```

## Discussion

With a `layoutDirection` of `leftToRight`, this is equivalent to right; and with a `layoutDirection` of `rightToLeft`, this is equivalent to left.

## See Also

### Getting the alignment

- [automatic](automatic.md) — The default column alignment.
- [leading](leading.md) — Leading column alignment.
- [center](center.md) — Center column alignment.
- [numeric](numeric.md) — Column alignment appropriate for numeric content.
- [numeric(_:)](<numeric(__).md>) — Column alignment appropriate for numeric content.
