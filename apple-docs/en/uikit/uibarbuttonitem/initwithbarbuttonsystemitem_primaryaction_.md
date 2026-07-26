---
title: 'initWithBarButtonSystemItem:primaryAction:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/initwithbarbuttonsystemitem:primaryaction:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithbarbuttonsystemitem:primaryaction:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/initwithbarbuttonsystemitem%3Aprimaryaction%3A.json'
content_hash: 'sha256:3ed6097a2a136d72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# initWithBarButtonSystemItem:primaryAction:

<sub>Instance Method</sub>

Creates an item using the specified system item and primary action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithBarButtonSystemItem:(UIBarButtonSystemItem) systemItem primaryAction:(UIAction *) primaryAction;
```

## Parameters

- `systemItem` — The system item to use as the first item on the bar. For possible values, see [SystemItem](systemitem.md).

- `primaryAction` — A [UIAction](../uiaction.md) to associate with the item. The system item doesn’t use the action to configure its title and image.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating system items

- [initWithBarButtonSystemItem:primaryAction:menu:](initwithbarbuttonsystemitem_primaryaction_menu_.md) — Creates an item using the specified system item, primary action, and context menu.
- [initWithBarButtonSystemItem:menu:](initwithbarbuttonsystemitem_menu_.md) — Creates an item using the specified system item and context menu.
- [- initWithBarButtonSystemItem:target:action:](<init(barbuttonsystemitem_target_action_).md>) — Creates an item using the specified system item, target, and action.
- [SystemItem](systemitem.md) — Constants that define system-supplied images for bar button items.
