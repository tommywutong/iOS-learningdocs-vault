---
title: 'creatingMovableGroup(customizationIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/creatingmovablegroup(customizationidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/creatingmovablegroup(customizationidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/creatingmovablegroup%28customizationidentifier%3A%29.json'
content_hash: 'sha256:e43a67c646c31bdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# creatingMovableGroup(customizationIdentifier:)

<sub>Instance Method</sub>

Places the item in a movable group that a person can move but can’t remove from the navigation bar during layout customization.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func creatingMovableGroup(customizationIdentifier: String) -> UIBarButtonItemGroup
```

## Parameters

- `customizationIdentifier` — A unique string to identify the group for navigation bar layout customization.

## Return Value

A [UIBarButtonItemGroup](../uibarbuttonitemgroup.md) that contains only this bar button item.

## Discussion

A bar button item can only belong to one [UIBarButtonItemGroup](../uibarbuttonitemgroup.md). If you add a bar button item to a new group, the system removes it from its previous group.

## See Also

### Creating groups

- [creatingOptionalGroup(customizationIdentifier:isInDefaultCustomization:)](<creatingoptionalgroup(customizationidentifier_isindefaultcustomization_).md>) — Places the item in an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [- creatingFixedGroup](<creatingfixedgroup().md>) — Places the item in a fixed group that a person can’t move or remove from the navigation bar during layout customization.
