---
title: 'fixedGroup(representativeItem:items:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemgroup/fixedgroup(representativeitem:items:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/fixedgroup(representativeitem:items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/fixedgroup%28representativeitem%3Aitems%3A%29.json'
content_hash: 'sha256:2baf12a282772489'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# fixedGroup(representativeItem:items:)

<sub>Type Method</sub>

Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency class func fixedGroup(representativeItem: UIBarButtonItem? = nil, items: [UIBarButtonItem]) -> UIBarButtonItemGroup
```

## Parameters

- `representativeItem` — The item to display for the group when space is constrained.

- `items` — The items to include in the group.

## See Also

### Creating a group

- [movableGroup(customizationIdentifier:representativeItem:items:)](<movablegroup(customizationidentifier_representativeitem_items_).md>) — Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [optionalGroup(customizationIdentifier:isInDefaultCustomization:representativeItem:items:)](<optionalgroup(customizationidentifier_isindefaultcustomization_representativeitem_items_).md>) — Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [- initWithBarButtonItems:representativeItem:](<init(barbuttonitems_representativeitem_).md>) — Creates a fixed group with the specified items.
- [- initWithCoder:](<init(coder_).md>) — Creates a bar button item group from data in an unarchiver.
