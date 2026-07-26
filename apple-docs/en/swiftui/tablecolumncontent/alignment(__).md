---
title: 'alignment(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumncontent/alignment(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncontent/alignment(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncontent/alignment%28_%3A%29.json'
content_hash: 'sha256:521dda9c6f429d4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnContent](../tablecolumncontent.md)

# alignment(_:)

<sub>Instance Method</sub>

Sets the alignment of the column, applying to both its column header label and the row view content for that column.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func alignment(_ alignment: TableColumnAlignment) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>

```

## Parameters

- `alignment` — The alignment to apply to the column.

## See Also

### Configuring the content

- [customizationID(_:)](<customizationid(__).md>) — Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.
- [defaultVisibility(_:)](<defaultvisibility(__).md>) — Sets the default visibility of a table column.
- [disabledCustomizationBehavior(_:)](<disabledcustomizationbehavior(__).md>) — Sets the disabled customization behavior for a table column.
