---
title: 'customizationID(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumncontent/customizationid(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncontent/customizationid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncontent/customizationid%28_%3A%29.json'
content_hash: 'sha256:7f42f7975328d366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnContent](../tablecolumncontent.md)

# customizationID(_:)

<sub>Instance Method</sub>

Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func customizationID(_ id: String) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>

```

## Parameters

- `id` — The identifier to associate with a column.

## Discussion

This is required to allow user customization of a specific table column, in addition to the table as a whole being provided a binding to a `TableColumnCustomization`.

The identifier needs to be stable, including across app version updates, since it is used to persist the user customization.

## See Also

### Configuring the content

- [alignment(_:)](<alignment(__).md>) — Sets the alignment of the column, applying to both its column header label and the row view content for that column.
- [defaultVisibility(_:)](<defaultvisibility(__).md>) — Sets the default visibility of a table column.
- [disabledCustomizationBehavior(_:)](<disabledcustomizationbehavior(__).md>) — Sets the disabled customization behavior for a table column.
