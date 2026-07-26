---
title: 'initWithPrimaryAction:menu:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/initwithprimaryaction:menu:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithprimaryaction:menu:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/initwithprimaryaction%3Amenu%3A.json'
content_hash: 'sha256:5f02fcbba67c895b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# initWithPrimaryAction:menu:

<sub>Instance Method</sub>

Creates a plain-style item using the specified primary action and context menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithPrimaryAction:(UIAction *) primaryAction menu:(UIMenu *) menu;
```

## Parameters

- `primaryAction` — A [UIAction](../uiaction.md) to associate with the item, which the item uses to configure its title and image.

- `menu` — The menu to present. The context menu displays in response to a person tapping the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating items

- [initWithPrimaryAction:](initwithprimaryaction_.md) — Creates a plain-style item using the specified primary action.
- [initWithTitle:image:target:action:menu:](initwithtitle_image_target_action_menu_.md) — Creates a plain-style item the specified title, image, target, action, and context menu.
- [initWithTitle:menu:](initwithtitle_menu_.md) — Creates a plain-style item using the specified title and menu.
- [initWithImage:menu:](initwithimage_menu_.md) — Creates a plain-style item using the specified image and context menu.
- [- init](<init().md>) — Initializes the item to its default state.
- [- initWithCoder:](<init(coder_).md>) — Creates an item from data in an unarchiver.
