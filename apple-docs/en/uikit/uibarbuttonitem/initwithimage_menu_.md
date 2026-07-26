---
title: 'initWithImage:menu:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/initwithimage:menu:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/initwithimage:menu:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/initwithimage%3Amenu%3A.json'
content_hash: 'sha256:222b4851a273f513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# initWithImage:menu:

<sub>Instance Method</sub>

Creates a plain-style item using the specified image and context menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithImage:(UIImage *) image menu:(UIMenu *) menu;
```

## Parameters

- `image` — The item’s image. If `nil`, an image doesn’t appear. The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.

- `menu` — The menu to present. The context menu displays in response to a person tapping the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating items

- [initWithPrimaryAction:menu:](initwithprimaryaction_menu_.md) — Creates a plain-style item using the specified primary action and context menu.
- [initWithPrimaryAction:](initwithprimaryaction_.md) — Creates a plain-style item using the specified primary action.
- [initWithTitle:image:target:action:menu:](initwithtitle_image_target_action_menu_.md) — Creates a plain-style item the specified title, image, target, action, and context menu.
- [initWithTitle:menu:](initwithtitle_menu_.md) — Creates a plain-style item using the specified title and menu.
- [- init](<init().md>) — Initializes the item to its default state.
- [- initWithCoder:](<init(coder_).md>) — Creates an item from data in an unarchiver.
