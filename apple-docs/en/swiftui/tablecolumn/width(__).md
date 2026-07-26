---
title: 'width(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumn/width(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/width(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/width%28_%3A%29.json'
content_hash: 'sha256:fb3f1681b96b3315'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# width(_:)

<sub>Instance Method</sub>

Creates a fixed width table column that isn’t user resizable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func width(_ width: CGFloat? = nil) -> TableColumn<RowValue, Sort, Content, Label>
```

## Parameters

- `width` — A fixed width for the resulting column. If `width` is `nil`, the resulting column has no change in sizing.

## See Also

### Setting the column width

- [width(min:ideal:max:)](<width(min_ideal_max_).md>) — Creates a resizable table column with the provided constraints.
- [width()](<width().md>) — Sets the column’s width. _(deprecated)_
