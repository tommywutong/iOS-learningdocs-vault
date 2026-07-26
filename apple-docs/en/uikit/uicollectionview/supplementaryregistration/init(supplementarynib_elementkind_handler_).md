---
title: 'init(supplementaryNib:elementKind:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionview/supplementaryregistration/init(supplementarynib:elementkind:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration/init(supplementarynib:elementkind:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/supplementaryregistration/init%28supplementarynib%3Aelementkind%3Ahandler%3A%29.json'
content_hash: 'sha256:bdaf0eb93c5228d9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [SupplementaryRegistration](../supplementaryregistration.md)

# init(supplementaryNib:elementKind:handler:)

<sub>Initializer</sub>

Creates a supplementary registration for the specified element kind with a registration handler and nib file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(supplementaryNib: UINib, elementKind: String, handler: @escaping UICollectionView.SupplementaryRegistration<Supplementary>.Handler)
```

## See Also

### Creating a supplementary registration

- [init(elementKind:handler:)](<init(elementkind_handler_).md>) — Creates a supplementary registration for the specified element kind with a registration handler.
- [Handler](handler.md) — A closure that handles the supplementary view registration and configuration.
