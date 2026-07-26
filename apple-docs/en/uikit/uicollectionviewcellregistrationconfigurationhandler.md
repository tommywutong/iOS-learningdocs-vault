---
title: UICollectionViewCellRegistrationConfigurationHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcellregistrationconfigurationhandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcellregistrationconfigurationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcellregistrationconfigurationhandler.json'
content_hash: 'sha256:fd066914b363fbd0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewCellRegistrationConfigurationHandler

<sub>Type Alias</sub>

A closure that handles the cell registration and configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(__kindof UICollectionViewCell *, NSIndexPath *, id) UICollectionViewCellRegistrationConfigurationHandler;
```

## Discussion

The closure takes the following parameters:

- **`cell`** — The [UICollectionViewCell](uicollectionviewcell.md) or subclass instance to configure.
- **`indexPath`** — The [IndexPath](../foundation/indexpath.md) of the cell to configure.
- **`item`** — The data item you provide in [dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:](uicollectionview/dequeueconfiguredreusablecellwithregistration_forindexpath_item_.md).

## See Also

### Creating a cell registration

- [registrationWithCellClass:configurationHandler:](uicollectionviewcellregistration/registrationwithcellclass_configurationhandler_.md) — Creates a cell registration with the specified registration handler.
- [registrationWithCellNib:configurationHandler:](uicollectionviewcellregistration/registrationwithcellnib_configurationhandler_.md) — Creates a cell registration with the specified registration handler and nib file.
