---
title: 'init(cellNib:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionview/cellregistration/init(cellnib:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration/init(cellnib:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/cellregistration/init%28cellnib%3Ahandler%3A%29.json'
content_hash: 'sha256:5e0afd51d3768964'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [CellRegistration](../cellregistration.md)

# init(cellNib:handler:)

<sub>Initializer</sub>

Creates a cell registration with the specified registration handler and nib file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(cellNib: UINib, handler: @escaping UICollectionView.CellRegistration<Cell, Item>.Handler)
```

## See Also

### Creating a cell registration

- [init(handler:)](<init(handler_).md>) — Creates a cell registration with the specified registration handler.
- [Handler](handler.md) — A closure that handles the cell registration and configuration.
