---
title: 'optionalGroup(customizationIdentifier:isInDefaultCustomization:representativeItem:items:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemgroup/optionalgroup(customizationidentifier:isindefaultcustomization:representativeitem:items:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/optionalgroup(customizationidentifier:isindefaultcustomization:representativeitem:items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/optionalgroup%28customizationidentifier%3Aisindefaultcustomization%3Arepresentativeitem%3Aitems%3A%29.json'
content_hash: 'sha256:f6e90b3af4bee26d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# optionalGroup(customizationIdentifier:isInDefaultCustomization:representativeItem:items:)

<sub>Type Method</sub>

Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency class func optionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool = true, representativeItem: UIBarButtonItem? = nil, items: [UIBarButtonItem]) -> UIBarButtonItemGroup
```

## Parameters

- `customizationIdentifier` — A unique string to identify the group for navigation bar layout customization.

- `isInDefaultCustomization` — A Boolean that determines whether to place the group in the navigation bar by default. Specify [false](../../swift/false.md) if you want the group to appear in the navigation bar customization popover by default.

- `representativeItem` — The item to display for the group when space is constrained.

- `items` — The items to include in the group.

## See Also

### Creating a group

- [fixedGroup(representativeItem:items:)](<fixedgroup(representativeitem_items_).md>) — Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [movableGroup(customizationIdentifier:representativeItem:items:)](<movablegroup(customizationidentifier_representativeitem_items_).md>) — Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [- initWithBarButtonItems:representativeItem:](<init(barbuttonitems_representativeitem_).md>) — Creates a fixed group with the specified items.
- [- initWithCoder:](<init(coder_).md>) — Creates a bar button item group from data in an unarchiver.
