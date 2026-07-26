---
title: 'initWithPrimaryAction:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/initwithprimaryaction:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithprimaryaction:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/initwithprimaryaction%3A.json'
content_hash: 'sha256:9b2d203f7668952f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# initWithPrimaryAction:

<sub>Instance Method</sub>

Creates a plain-style item using the specified primary action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithPrimaryAction:(UIAction *) primaryAction;
```

## Parameters

- `primaryAction` — A [UIAction](../uiaction.md) to associate with the item, which the item uses to configure its title and image.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating items

- [initWithPrimaryAction:menu:](initwithprimaryaction_menu_.md) — Creates a plain-style item using the specified primary action and context menu.
- [initWithTitle:image:target:action:menu:](initwithtitle_image_target_action_menu_.md) — Creates a plain-style item the specified title, image, target, action, and context menu.
- [initWithTitle:menu:](initwithtitle_menu_.md) — Creates a plain-style item using the specified title and menu.
- [initWithImage:menu:](initwithimage_menu_.md) — Creates a plain-style item using the specified image and context menu.
- [- init](<init().md>) — Initializes the item to its default state.
- [- initWithCoder:](<init(coder_).md>) — Creates an item from data in an unarchiver.
