---
title: 'init(handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/cellregistration/init(handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration/init(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/cellregistration/init%28handler%3A%29.json'
content_hash: 'sha256:0653f438be4d17fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [CellRegistration](../cellregistration.md)

# init(handler:)

<sub>Initializer</sub>

Creates a cell registration with the specified registration handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(handler: @escaping UICollectionView.CellRegistration<Cell, Item>.Handler)
```

## See Also

### Creating a cell registration

- [init(cellNib:handler:)](<init(cellnib_handler_).md>) — Creates a cell registration with the specified registration handler and nib file.
- [Handler](handler.md) — A closure that handles the cell registration and configuration.
