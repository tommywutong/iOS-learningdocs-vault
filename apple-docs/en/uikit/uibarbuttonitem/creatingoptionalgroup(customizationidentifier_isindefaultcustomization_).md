---
title: 'creatingOptionalGroup(customizationIdentifier:isInDefaultCustomization:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/creatingoptionalgroup(customizationidentifier:isindefaultcustomization:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/creatingoptionalgroup(customizationidentifier:isindefaultcustomization:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/creatingoptionalgroup%28customizationidentifier%3Aisindefaultcustomization%3A%29.json'
content_hash: 'sha256:f7824e2cd3ec50a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# creatingOptionalGroup(customizationIdentifier:isInDefaultCustomization:)

<sub>Instance Method</sub>

Places the item in an optional group that a person can move, add to, or remove from the navigation bar during layout customization.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func creatingOptionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool = true) -> UIBarButtonItemGroup
```

## Parameters

- `customizationIdentifier` — A unique string to identify the group for navigation bar layout customization.

- `isInDefaultCustomization` — A Boolean that determines whether to place the group in the navigation bar by default. Specify [false](../../swift/false.md) if you want the group to appear in the navigation bar customization popover by default.

## Return Value

A [UIBarButtonItemGroup](../uibarbuttonitemgroup.md) that contains only this bar button item.

## Discussion

A bar button item can only belong to one [UIBarButtonItemGroup](../uibarbuttonitemgroup.md). If you add a bar button item to a new group, the system removes it from its previous group.

## See Also

### Creating groups

- [- creatingFixedGroup](<creatingfixedgroup().md>) — Places the item in a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [- creatingMovableGroupWithCustomizationIdentifier:](<creatingmovablegroup(customizationidentifier_).md>) — Places the item in a movable group that a person can move but can’t remove from the navigation bar during layout customization.
