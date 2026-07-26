---
title: width()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/tablecolumn/width()
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/width()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/width%28%29.json'
content_hash: 'sha256:529d17f300ca1376'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# width()

<sub>Instance Method</sub>

Sets the column’s width.

> [!warning] Deprecated
> Use [width(_:)](<width(__).md>) or [width(min:ideal:max:)](<width(min_ideal_max_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func width() -> TableColumn<RowValue, Sort, Content, Label>
```

## See Also

### Setting the column width

- [width(_:)](<width(__).md>) — Creates a fixed width table column that isn’t user resizable.
- [width(min:ideal:max:)](<width(min_ideal_max_).md>) — Creates a resizable table column with the provided constraints.
