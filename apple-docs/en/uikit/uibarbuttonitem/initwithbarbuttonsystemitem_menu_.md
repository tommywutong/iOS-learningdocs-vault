---
title: 'initWithBarButtonSystemItem:menu:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/initwithbarbuttonsystemitem:menu:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithbarbuttonsystemitem:menu:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/initwithbarbuttonsystemitem%3Amenu%3A.json'
content_hash: 'sha256:eb2e6994d0493720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# initWithBarButtonSystemItem:menu:

<sub>Instance Method</sub>

Creates an item using the specified system item and context menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithBarButtonSystemItem:(UIBarButtonSystemItem) systemItem menu:(UIMenu *) menu;
```

## Parameters

- `systemItem` — The system item to use as the first item on the bar. For possible values, see [SystemItem](systemitem.md).

- `menu` — The menu to present. The context menu displays in response to a person tapping the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating system items

- [initWithBarButtonSystemItem:primaryAction:menu:](initwithbarbuttonsystemitem_primaryaction_menu_.md) — Creates an item using the specified system item, primary action, and context menu.
- [initWithBarButtonSystemItem:primaryAction:](initwithbarbuttonsystemitem_primaryaction_.md) — Creates an item using the specified system item and primary action.
- [- initWithBarButtonSystemItem:target:action:](<init(barbuttonsystemitem_target_action_).md>) — Creates an item using the specified system item, target, and action.
- [SystemItem](systemitem.md) — Constants that define system-supplied images for bar button items.
