---
title: UICollectionView.SupplementaryRegistration.Handler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/supplementaryregistration/handler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration/handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/supplementaryregistration/handler.json'
content_hash: 'sha256:37d368d8e35b23b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionView](../../uicollectionview.md) · [SupplementaryRegistration](../supplementaryregistration.md)

# UICollectionView.SupplementaryRegistration.Handler

<sub>Type Alias</sub>

A closure that handles the supplementary view registration and configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias Handler = (Supplementary, String, IndexPath) -> Void
```

## See Also

### Creating a supplementary registration

- [init(elementKind:handler:)](<init(elementkind_handler_).md>) — Creates a supplementary registration for the specified element kind with a registration handler.
- [init(supplementaryNib:elementKind:handler:)](<init(supplementarynib_elementkind_handler_).md>) — Creates a supplementary registration for the specified element kind with a registration handler and nib file.
