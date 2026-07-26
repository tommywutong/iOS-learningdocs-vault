---
title: 'width(min:ideal:max:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumn/width(min:ideal:max:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumn/width(min:ideal:max:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumn/width%28min%3Aideal%3Amax%3A%29.json'
content_hash: 'sha256:ef9aa50cd3e702d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumn](../tablecolumn.md)

# width(min:ideal:max:)

<sub>Instance Method</sub>

Creates a resizable table column with the provided constraints.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func width(min: CGFloat? = nil, ideal: CGFloat? = nil, max: CGFloat? = nil) -> TableColumn<RowValue, Sort, Content, Label>
```

## Parameters

- `min` — The minimum width of a resizable column. If non-`nil`, the value must be greater than or equal to `0`.

- `ideal` — The ideal width of the column, used to determine the initial width of the table column. The column always starts at least as large as the set ideal size, but may be larger if table was sized larger than the ideal of all of its columns.

- `max` — The maximum width of a resizable column. If non-`nil`, the value must be greater than `0`. Pass [infinity](../../swift/floatingpoint/infinity.md) to indicate unconstrained maximum width.

## Discussion

Always specify at least one width constraint when calling this method. Pass `nil` or leave out a constraint to indicate no change to the sizing of a column.

To create a fixed size column use [width(_:)](<width(__).md>) instead.

## See Also

### Setting the column width

- [width(_:)](<width(__).md>) — Creates a fixed width table column that isn’t user resizable.
- [width()](<width().md>) — Sets the column’s width. _(deprecated)_
