---
title: 'registrationWithCellClass:configurationHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewcellregistration/registrationwithcellclass:configurationhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcellregistration/registrationwithcellclass:configurationhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcellregistration/registrationwithcellclass%3Aconfigurationhandler%3A.json'
content_hash: 'sha256:c1b92369498383b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCellRegistration](../uicollectionviewcellregistration.md)

# registrationWithCellClass:configurationHandler:

<sub>Type Method</sub>

Creates a cell registration with the specified registration handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) registrationWithCellClass:(Class) cellClass configurationHandler:(UICollectionViewCellRegistrationConfigurationHandler) configurationHandler;
```

## See Also

### Creating a cell registration

- [registrationWithCellNib:configurationHandler:](registrationwithcellnib_configurationhandler_.md) — Creates a cell registration with the specified registration handler and nib file.
- [UICollectionViewCellRegistrationConfigurationHandler](../uicollectionviewcellregistrationconfigurationhandler.md) — A closure that handles the cell registration and configuration.
