---
title: 'accessibilityDataTableCellElement(forRow:column:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilitydatatablecellelement(forrow:column:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilitydatatablecellelement(forrow:column:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilitydatatablecellelement%28forrow%3Acolumn%3A%29.json'
content_hash: 'sha256:862b9af27432dc9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityContainerDataTable](../uiaccessibilitycontainerdatatable.md)

# accessibilityDataTableCellElement(forRow:column:)

<sub>Instance Method</sub>

Returns the accessibility element for the specified cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func accessibilityDataTableCellElement(forRow row: Int, column: Int) -> (any UIAccessibilityContainerDataTableCell)?
```

## Parameters

- `row` — The row of the cell.

- `column` — The column of the cell.

## Return Value

The accessibility element for the cell.
