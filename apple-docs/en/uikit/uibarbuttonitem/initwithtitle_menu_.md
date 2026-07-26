---
title: 'initWithTitle:menu:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/initwithtitle:menu:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithtitle:menu:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/initwithtitle%3Amenu%3A.json'
content_hash: 'sha256:c7f2a295c207b4f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# initWithTitle:menu:

<sub>Instance Method</sub>

Creates a plain-style item using the specified title and menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithTitle:(NSString *) title menu:(UIMenu *) menu;
```

## Parameters

- `title` — The item’s title. If `nil`, a title doesn’t appear.

- `menu` — The menu to present. The context menu displays in response to a person tapping the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating items

- [initWithPrimaryAction:menu:](initwithprimaryaction_menu_.md) — Creates a plain-style item using the specified primary action and context menu.
- [initWithPrimaryAction:](initwithprimaryaction_.md) — Creates a plain-style item using the specified primary action.
- [initWithTitle:image:target:action:menu:](initwithtitle_image_target_action_menu_.md) — Creates a plain-style item the specified title, image, target, action, and context menu.
- [initWithImage:menu:](initwithimage_menu_.md) — Creates a plain-style item using the specified image and context menu.
- [- init](<init().md>) — Initializes the item to its default state.
- [- initWithCoder:](<init(coder_).md>) — Creates an item from data in an unarchiver.
