---
title: 'fixedGroupWithRepresentativeItem:items:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemgroup/fixedgroupwithrepresentativeitem:items:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/fixedgroupwithrepresentativeitem:items:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/fixedgroupwithrepresentativeitem%3Aitems%3A.json'
content_hash: 'sha256:6bb1372a541c37a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# fixedGroupWithRepresentativeItem:items:

<sub>Type Method</sub>

Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIBarButtonItemGroup *) fixedGroupWithRepresentativeItem:(UIBarButtonItem *) representativeItem items:(NSArray<UIBarButtonItem *> *) items;
```

## Parameters

- `representativeItem` — The item to display for the group when space is constrained.

- `items` — The items to include in the group.

## See Also

### Creating a group

- [movableGroupWithCustomizationIdentifier:representativeItem:items:](movablegroupwithcustomizationidentifier_representativeitem_items_.md) — Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [optionalGroupWithCustomizationIdentifier:inDefaultCustomization:representativeItem:items:](optionalgroupwithcustomizationidentifier_indefaultcustomization_representativeitem_items_.md) — Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [- initWithBarButtonItems:representativeItem:](<init(barbuttonitems_representativeitem_).md>) — Creates a fixed group with the specified items.
- [- initWithCoder:](<init(coder_).md>) — Creates a bar button item group from data in an unarchiver.
