---
title: 'registrationWithSupplementaryClass:elementKind:configurationHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementaryclass:elementkind:configurationhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementaryclass:elementkind:configurationhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewsupplementaryregistration/registrationwithsupplementaryclass%3Aelementkind%3Aconfigurationhandler%3A.json'
content_hash: 'sha256:f2c50ff147b966df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewSupplementaryRegistration](../uicollectionviewsupplementaryregistration.md)

# registrationWithSupplementaryClass:elementKind:configurationHandler:

<sub>Type Method</sub>

Creates a supplementary registration for the specified element kind with a registration handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) registrationWithSupplementaryClass:(Class) supplementaryClass elementKind:(NSString *) elementKind configurationHandler:(UICollectionViewSupplementaryRegistrationConfigurationHandler) configurationHandler;
```

## See Also

### Creating a supplementary registration

- [registrationWithSupplementaryNib:elementKind:configurationHandler:](registrationwithsupplementarynib_elementkind_configurationhandler_.md) — Creates a supplementary registration for the specified element kind with a registration handler and nib file.
- [UICollectionViewSupplementaryRegistrationConfigurationHandler](../uicollectionviewsupplementaryregistrationconfigurationhandler.md) — A block that handles the supplementary view registration and configuration.
