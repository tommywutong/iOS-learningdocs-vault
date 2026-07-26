---
title: 'optionalGroupWithCustomizationIdentifier:inDefaultCustomization:representativeItem:items:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemgroup/optionalgroupwithcustomizationidentifier:indefaultcustomization:representativeitem:items:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/optionalgroupwithcustomizationidentifier:indefaultcustomization:representativeitem:items:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/optionalgroupwithcustomizationidentifier%3Aindefaultcustomization%3Arepresentativeitem%3Aitems%3A.json'
content_hash: 'sha256:d56e89a1f238cdcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# optionalGroupWithCustomizationIdentifier:inDefaultCustomization:representativeItem:items:

<sub>Type Method</sub>

Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIBarButtonItemGroup *) optionalGroupWithCustomizationIdentifier:(NSString *) customizationIdentifier inDefaultCustomization:(BOOL) inDefaultCustomization representativeItem:(UIBarButtonItem *) representativeItem items:(NSArray<UIBarButtonItem *> *) items;
```

## Parameters

- `customizationIdentifier` — A unique string to identify the group for navigation bar layout customization.

- `inDefaultCustomization` — A Boolean that determines whether to place the group in the navigation bar by default. Specify [false](../../swift/false.md) if you want the group to appear in the navigation bar customization popover by default.

- `representativeItem` — The item to display for the group when space is constrained.

- `items` — The items to include in the group.

## See Also

### Creating a group

- [fixedGroupWithRepresentativeItem:items:](fixedgroupwithrepresentativeitem_items_.md) — Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [movableGroupWithCustomizationIdentifier:representativeItem:items:](movablegroupwithcustomizationidentifier_representativeitem_items_.md) — Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [- initWithBarButtonItems:representativeItem:](<init(barbuttonitems_representativeitem_).md>) — Creates a fixed group with the specified items.
- [- initWithCoder:](<init(coder_).md>) — Creates a bar button item group from data in an unarchiver.
