---
title: 'accessibilityHeaderElements(forRow:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements(forrow:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements(forrow:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements%28forrow%3A%29.json'
content_hash: 'sha256:45c7808e216019a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityContainerDataTable](../uiaccessibilitycontainerdatatable.md)

# accessibilityHeaderElements(forRow:)

<sub>Instance Method</sub>

Returns the accessibility element for the specified row header.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func accessibilityHeaderElements(forRow row: Int) -> [any UIAccessibilityContainerDataTableCell]?
```

## Parameters

- `row` — The index of the row containing the header.

## Return Value

The accessibility elements for the specified row header.

## See Also

### Providing header elements

- [- accessibilityHeaderElementsForColumn:](<accessibilityheaderelements(forcolumn_).md>) — Returns the accessibility element for the specified column header.
