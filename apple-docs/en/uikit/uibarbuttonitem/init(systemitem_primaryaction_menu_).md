---
title: 'init(systemItem:primaryAction:menu:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(systemitem:primaryaction:menu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(systemitem:primaryaction:menu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28systemitem%3Aprimaryaction%3Amenu%3A%29.json'
content_hash: 'sha256:3cbf6aa790b262ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(systemItem:primaryAction:menu:)

<sub>Initializer</sub>

Creates an item using the specified system item, primary action, and context menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(systemItem: UIBarButtonItem.SystemItem, primaryAction: UIAction? = nil, menu: UIMenu? = nil)
```

## Parameters

- `systemItem` — The system item to use as the first item on the bar. For possible values, see [SystemItem](systemitem.md).

- `primaryAction` — A [UIAction](../uiaction.md) to associate with the item. The system item doesn’t use the action to configure its title and image.

- `menu` — The menu to present. The context menu displays in response to a person tapping the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating system items

- [- initWithBarButtonSystemItem:target:action:](<init(barbuttonsystemitem_target_action_).md>) — Creates an item using the specified system item, target, and action.
- [SystemItem](systemitem.md) — Constants that define system-supplied images for bar button items.
