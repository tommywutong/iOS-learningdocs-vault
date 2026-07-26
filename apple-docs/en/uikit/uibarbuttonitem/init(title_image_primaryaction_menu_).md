---
title: 'init(title:image:primaryAction:menu:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(title:image:primaryaction:menu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(title:image:primaryaction:menu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28title%3Aimage%3Aprimaryaction%3Amenu%3A%29.json'
content_hash: 'sha256:32d389b72954f90e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(title:image:primaryAction:menu:)

<sub>Initializer</sub>

Creates a plain-style item using the specified title, image, primary action, and context menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(title: String? = nil, image: UIImage? = nil, primaryAction: UIAction? = nil, menu: UIMenu? = nil)
```

## Parameters

- `title` — The item’s title.

- `image` — The item’s image. The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.

- `primaryAction` — A [UIAction](../uiaction.md) to associate with the item, which the item uses to configure its title and image. If you specify `primaryAction`, it takes precedence over `title` and `image`.

- `menu` — The menu to present. The context menu displays in response to a person tapping the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating items

- [init(title:image:target:action:menu:)](<init(title_image_target_action_menu_).md>) — Creates a plain-style item using the specified title, image, target, action, and context menu.
- [- init](<init().md>) — Initializes the item to its default state.
- [- initWithCoder:](<init(coder_).md>) — Creates an item from data in an unarchiver.
