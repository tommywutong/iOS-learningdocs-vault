---
title: 'init(elementKind:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/supplementaryregistration/init(elementkind:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration/init(elementkind:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/supplementaryregistration/init%28elementkind%3Ahandler%3A%29.json'
content_hash: 'sha256:91253f964c3144d8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [SupplementaryRegistration](../supplementaryregistration.md)

# init(elementKind:handler:)

<sub>Initializer</sub>

Creates a supplementary registration for the specified element kind with a registration handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(elementKind: String, handler: @escaping UICollectionView.SupplementaryRegistration<Supplementary>.Handler)
```

## See Also

### Creating a supplementary registration

- [init(supplementaryNib:elementKind:handler:)](<init(supplementarynib_elementkind_handler_).md>) — Creates a supplementary registration for the specified element kind with a registration handler and nib file.
- [Handler](handler.md) — A closure that handles the supplementary view registration and configuration.
