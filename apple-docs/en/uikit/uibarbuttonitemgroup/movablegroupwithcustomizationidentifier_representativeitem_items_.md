---
title: 'movableGroupWithCustomizationIdentifier:representativeItem:items:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemgroup/movablegroupwithcustomizationidentifier:representativeitem:items:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/movablegroupwithcustomizationidentifier:representativeitem:items:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/movablegroupwithcustomizationidentifier%3Arepresentativeitem%3Aitems%3A.json'
content_hash: 'sha256:b7222afdcdf4fba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# movableGroupWithCustomizationIdentifier:representativeItem:items:

<sub>Type Method</sub>

Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIBarButtonItemGroup *) movableGroupWithCustomizationIdentifier:(NSString *) customizationIdentifier representativeItem:(UIBarButtonItem *) representativeItem items:(NSArray<UIBarButtonItem *> *) items;
```

## Parameters

- `customizationIdentifier` — A unique string to identify the group for navigation bar layout customization.

- `representativeItem` — The item to display for the group when space is constrained.

- `items` — The items to include in the group.

## See Also

### Creating a group

- [fixedGroupWithRepresentativeItem:items:](fixedgroupwithrepresentativeitem_items_.md) — Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [optionalGroupWithCustomizationIdentifier:inDefaultCustomization:representativeItem:items:](optionalgroupwithcustomizationidentifier_indefaultcustomization_representativeitem_items_.md) — Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [- initWithBarButtonItems:representativeItem:](<init(barbuttonitems_representativeitem_).md>) — Creates a fixed group with the specified items.
- [- initWithCoder:](<init(coder_).md>) — Creates a bar button item group from data in an unarchiver.
