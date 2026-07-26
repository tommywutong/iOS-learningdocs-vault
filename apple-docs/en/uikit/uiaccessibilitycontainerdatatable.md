---
title: UIAccessibilityContainerDataTable
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontainerdatatable
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainerdatatable.json'
content_hash: 'sha256:47c4e0d75e4de551'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityContainerDataTable

<sub>Protocol</sub>

Methods that convey information about the contents of a table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIAccessibilityContainerDataTable : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing cell elements

- [- accessibilityDataTableCellElementForRow:column:](<uiaccessibilitycontainerdatatable/accessibilitydatatablecellelement(forrow_column_).md>) — Returns the accessibility element for the specified cell.

### Providing the table dimensions

- [- accessibilityColumnCount](<uiaccessibilitycontainerdatatable/accessibilitycolumncount().md>) — Returns the total number of columns in the table.
- [- accessibilityRowCount](<uiaccessibilitycontainerdatatable/accessibilityrowcount().md>) — Returns the total number of rows in the table.

### Providing header elements

- [- accessibilityHeaderElementsForColumn:](<uiaccessibilitycontainerdatatable/accessibilityheaderelements(forcolumn_).md>) — Returns the accessibility element for the specified column header.
- [- accessibilityHeaderElementsForRow:](<uiaccessibilitycontainerdatatable/accessibilityheaderelements(forrow_).md>) — Returns the accessibility element for the specified row header.

## See Also

### Containers

- [UIAccessibilityContainerDataTableCell](uiaccessibilitycontainerdatatablecell.md) — Methods that provide the location of a cell in a table.
- [UIAccessibilityContainerType](uiaccessibilitycontainertype.md) — Constants that indicate the type of content in a data-based container.
