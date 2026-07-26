---
title: UICollectionView.CellRegistration.Handler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/cellregistration/handler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration/handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/cellregistration/handler.json'
content_hash: 'sha256:f7882c1662c80ffd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [CellRegistration](../cellregistration.md)

# UICollectionView.CellRegistration.Handler

<sub>Type Alias</sub>

A closure that handles the cell registration and configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias Handler = (Cell, IndexPath, Item) -> Void
```

## Discussion

The closure takes the following parameters:

- **`cell`** — The [UICollectionViewCell](../../uicollectionviewcell.md) or subclass instance to configure.
- **`indexPath`** — The [IndexPath](../../../foundation/indexpath.md) of the cell to configure.
- **`item`** — The data item you provide in [dequeueConfiguredReusableCell(using:for:item:)](<../dequeueconfiguredreusablecell(using_for_item_).md>).

## See Also

### Creating a cell registration

- [init(handler:)](<init(handler_).md>) — Creates a cell registration with the specified registration handler.
- [init(cellNib:handler:)](<init(cellnib_handler_).md>) — Creates a cell registration with the specified registration handler and nib file.
