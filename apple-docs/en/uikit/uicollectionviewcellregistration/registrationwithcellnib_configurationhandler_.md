---
title: 'registrationWithCellNib:configurationHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+（1.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionviewcellregistration/registrationwithcellnib:configurationhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcellregistration/registrationwithcellnib:configurationhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcellregistration/registrationwithcellnib%3Aconfigurationhandler%3A.json'
content_hash: 'sha256:94568e99cb11a9be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCellRegistration](../uicollectionviewcellregistration.md)

# registrationWithCellNib:configurationHandler:

<sub>Type Method</sub>

Creates a cell registration with the specified registration handler and nib file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) registrationWithCellNib:(UINib *) cellNib configurationHandler:(UICollectionViewCellRegistrationConfigurationHandler) configurationHandler;
```

## See Also

### Creating a cell registration

- [registrationWithCellClass:configurationHandler:](registrationwithcellclass_configurationhandler_.md) — Creates a cell registration with the specified registration handler.
- [UICollectionViewCellRegistrationConfigurationHandler](../uicollectionviewcellregistrationconfigurationhandler.md) — A closure that handles the cell registration and configuration.
