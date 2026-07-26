---
title: 'accessibilityHeaderElements(forColumn:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements(forcolumn:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements(forcolumn:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements%28forcolumn%3A%29.json'
content_hash: 'sha256:4756c5330c33a950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityContainerDataTable](../uiaccessibilitycontainerdatatable.md)

# accessibilityHeaderElements(forColumn:)

<sub>Instance Method</sub>

Returns the accessibility element for the specified column header.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func accessibilityHeaderElements(forColumn column: Int) -> [any UIAccessibilityContainerDataTableCell]?
```

## Parameters

- `column` — The index of the column containing the header.

## Return Value

The accessibility elements for the specified column header.

## See Also

### Providing header elements

- [- accessibilityHeaderElementsForRow:](<accessibilityheaderelements(forrow_).md>) — Returns the accessibility element for the specified row header.
