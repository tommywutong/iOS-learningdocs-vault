---
title: 'defaultVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumncontent/defaultvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncontent/defaultvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncontent/defaultvisibility%28_%3A%29.json'
content_hash: 'sha256:be656aa6bfbfeba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnContent](../tablecolumncontent.md)

# defaultVisibility(_:)

<sub>Instance Method</sub>

Sets the default visibility of a table column.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func defaultVisibility(_ visibility: Visibility) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>

```

## Parameters

- `visibility` — The default visibility to apply to columns.

## Discussion

A `hidden` column will not be visible, unless the `Table` is also bound to `TableColumnCustomization` and either modified programmatically or by the user.

## See Also

### Configuring the content

- [alignment(_:)](<alignment(__).md>) — Sets the alignment of the column, applying to both its column header label and the row view content for that column.
- [customizationID(_:)](<customizationid(__).md>) — Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.
- [disabledCustomizationBehavior(_:)](<disabledcustomizationbehavior(__).md>) — Sets the disabled customization behavior for a table column.
