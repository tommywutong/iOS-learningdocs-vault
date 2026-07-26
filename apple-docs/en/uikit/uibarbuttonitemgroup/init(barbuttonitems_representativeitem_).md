---
title: 'init(barButtonItems:representativeItem:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemgroup/init(barbuttonitems:representativeitem:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/init(barbuttonitems:representativeitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/init%28barbuttonitems%3Arepresentativeitem%3A%29.json'
content_hash: 'sha256:aea9d9353b975d50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# init(barButtonItems:representativeItem:)

<sub>Initializer</sub>

Creates a fixed group with the specified items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(barButtonItems: [UIBarButtonItem], representativeItem: UIBarButtonItem?)
```

## Parameters

- `barButtonItems` — The bar button items to display on the bar. Typically, the items in a group are related to each other in some way, although that need not be the case. You must not specify an empty array.

- `representativeItem` — A bar button item to display when there isn’t enough room to display the items in `barButtonItems`. The object you specify must be distinct from the objects in the `barButtonItems` parameter. It’s a programmer error to specify an object that’s also in the array passed to the `barButtonItems` parameter. You may specify `nil` for this parameter.

## Return Value

An initialized bar button item group.

## Discussion

When you use this initializer to create a group for a navigation bar, it produces the same result as [fixedGroup(representativeItem:items:)](<fixedgroup(representativeitem_items_).md>) (Swift) or [fixedGroupWithRepresentativeItem:items:](fixedgroupwithrepresentativeitem_items_.md) (Objective-C).

When you use this initializer to create a group for the shortcuts bar, use the resulting group object to configure the [leadingBarButtonGroups](../uitextinputassistantitem/leadingbarbuttongroups.md) or [trailingBarButtonGroups](../uitextinputassistantitem/trailingbarbuttongroups.md) property of a [UITextInputAssistantItem](../uitextinputassistantitem.md) object.

## See Also

### Creating a group

- [fixedGroup(representativeItem:items:)](<fixedgroup(representativeitem_items_).md>) — Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [movableGroup(customizationIdentifier:representativeItem:items:)](<movablegroup(customizationidentifier_representativeitem_items_).md>) — Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [optionalGroup(customizationIdentifier:isInDefaultCustomization:representativeItem:items:)](<optionalgroup(customizationidentifier_isindefaultcustomization_representativeitem_items_).md>) — Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [- initWithCoder:](<init(coder_).md>) — Creates a bar button item group from data in an unarchiver.
