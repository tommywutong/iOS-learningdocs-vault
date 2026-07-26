---
title: 'init(barButtonSystemItem:target:action:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(barbuttonsystemitem:target:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(barbuttonsystemitem:target:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28barbuttonsystemitem%3Atarget%3Aaction%3A%29.json'
content_hash: 'sha256:ad7092e0049bb887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(barButtonSystemItem:target:action:)

<sub>Initializer</sub>

Creates an item using the specified system item, target, and action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(barButtonSystemItem systemItem: UIBarButtonItem.SystemItem, target: Any?, action: Selector?)
```

## Parameters

- `systemItem` — The system item to use as the first item on the bar. For possible values, see [SystemItem](systemitem.md).

- `target` — The object that receives the `action` message.

- `action` — The action to send to `target` when a person selects this item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Related Documentation

- [- initWithImage:style:target:action:](<init(image_style_target_action_).md>) — Creates an item using the specified image, style, target, and action.
- [- initWithTitle:style:target:action:](<init(title_style_target_action_).md>) — Creates an item using the specified title, style, target, and action.

### Creating system items

- [init(systemItem:primaryAction:menu:)](<init(systemitem_primaryaction_menu_).md>) — Creates an item using the specified system item, primary action, and context menu.
- [SystemItem](systemitem.md) — Constants that define system-supplied images for bar button items.
