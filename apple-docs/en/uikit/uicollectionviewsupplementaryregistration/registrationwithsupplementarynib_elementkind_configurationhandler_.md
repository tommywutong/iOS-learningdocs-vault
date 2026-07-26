---
title: 'registrationWithSupplementaryNib:elementKind:configurationHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+（1.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementarynib:elementkind:configurationhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementarynib:elementkind:configurationhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementarynib%3Aelementkind%3Aconfigurationhandler%3A.json'
content_hash: 'sha256:6ca84d80aed1d837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewSupplementaryRegistration](../uicollectionviewsupplementaryregistration.md)

# registrationWithSupplementaryNib:elementKind:configurationHandler:

<sub>Type Method</sub>

Creates a supplementary registration for the specified element kind with a registration handler and nib file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) registrationWithSupplementaryNib:(UINib *) supplementaryNib elementKind:(NSString *) elementKind configurationHandler:(UICollectionViewSupplementaryRegistrationConfigurationHandler) configurationHandler;
```

## See Also

### Creating a supplementary registration

- [registrationWithSupplementaryClass:elementKind:configurationHandler:](registrationwithsupplementaryclass_elementkind_configurationhandler_.md) — Creates a supplementary registration for the specified element kind with a registration handler.
- [UICollectionViewSupplementaryRegistrationConfigurationHandler](../uicollectionviewsupplementaryregistrationconfigurationhandler.md) — A block that handles the supplementary view registration and configuration.
