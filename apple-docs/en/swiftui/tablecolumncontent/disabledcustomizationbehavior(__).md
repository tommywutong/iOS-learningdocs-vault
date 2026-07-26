---
title: 'disabledCustomizationBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumncontent/disabledcustomizationbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumncontent/disabledcustomizationbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumncontent/disabledcustomizationbehavior%28_%3A%29.json'
content_hash: 'sha256:69abfaed9df3a7f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnContent](../tablecolumncontent.md)

# disabledCustomizationBehavior(_:)

<sub>Instance Method</sub>

Sets the disabled customization behavior for a table column.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func disabledCustomizationBehavior(_ behavior: TableColumnCustomizationBehavior) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>

```

## Parameters

- `behavior` — The behavior to disable, or `.all` to not allow any customization.

## Discussion

When the containing `Table` is bound to some `TableColumnCustomization`, all columns will be able to be customized by the user on macOS by default (i.e. `TableColumnCustomizationBehavior.all`). This modifier allows disabling specific behavior.

This modifier has no effect on iOS since `Table` does not support any built-in user customization features.

This does not prevent programmatic changes to a table column customization.

## See Also

### Configuring the content

- [alignment(_:)](<alignment(__).md>) — Sets the alignment of the column, applying to both its column header label and the row view content for that column.
- [customizationID(_:)](<customizationid(__).md>) — Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.
- [defaultVisibility(_:)](<defaultvisibility(__).md>) — Sets the default visibility of a table column.
