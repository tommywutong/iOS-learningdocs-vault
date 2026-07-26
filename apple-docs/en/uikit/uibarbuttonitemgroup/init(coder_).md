---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitemgroup/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemgroup/init%28coder%3A%29.json'
content_hash: 'sha256:dc7a42e6f2dc069a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemGroup](../uibarbuttonitemgroup.md)

# init(coder:)

<sub>Initializer</sub>

Creates a bar button item group from data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## See Also

### Creating a group

- [fixedGroup(representativeItem:items:)](<fixedgroup(representativeitem_items_).md>) — Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [movableGroup(customizationIdentifier:representativeItem:items:)](<movablegroup(customizationidentifier_representativeitem_items_).md>) — Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [optionalGroup(customizationIdentifier:isInDefaultCustomization:representativeItem:items:)](<optionalgroup(customizationidentifier_isindefaultcustomization_representativeitem_items_).md>) — Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [- initWithBarButtonItems:representativeItem:](<init(barbuttonitems_representativeitem_).md>) — Creates a fixed group with the specified items.
