---
title: UICollectionViewSupplementaryRegistrationConfigurationHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewsupplementaryregistrationconfigurationhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewsupplementaryregistrationconfigurationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewsupplementaryregistrationconfigurationhandler.json'
content_hash: 'sha256:9c388a698ce171cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewSupplementaryRegistrationConfigurationHandler

<sub>Type Alias</sub>

A block that handles the supplementary view registration and configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(__kindof UICollectionReusableView *, NSString *, NSIndexPath *) UICollectionViewSupplementaryRegistrationConfigurationHandler;
```

## See Also

### Creating a supplementary registration

- [registrationWithSupplementaryClass:elementKind:configurationHandler:](uicollectionviewsupplementaryregistration/registrationwithsupplementaryclass_elementkind_configurationhandler_.md) — Creates a supplementary registration for the specified element kind with a registration handler.
- [registrationWithSupplementaryNib:elementKind:configurationHandler:](uicollectionviewsupplementaryregistration/registrationwithsupplementarynib_elementkind_configurationhandler_.md) — Creates a supplementary registration for the specified element kind with a registration handler and nib file.
