---
title: UIAccessibilityContainerDataTableCell
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontainerdatatablecell
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainerdatatablecell.json'
content_hash: 'sha256:76792bea0d33f68a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityContainerDataTableCell

<sub>Protocol</sub>

Methods that provide the location of a cell in a table.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIAccessibilityContainerDataTableCell : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the rows and columns

- [- accessibilityColumnRange](<uiaccessibilitycontainerdatatablecell/accessibilitycolumnrange().md>) — Returns the columns spanned by the cell.
- [- accessibilityRowRange](<uiaccessibilitycontainerdatatablecell/accessibilityrowrange().md>) — Returns the visible range of rows.

## See Also

### Containers

- [UIAccessibilityContainerDataTable](uiaccessibilitycontainerdatatable.md) — Methods that convey information about the contents of a table.
- [UIAccessibilityContainerType](uiaccessibilitycontainertype.md) — Constants that indicate the type of content in a data-based container.
