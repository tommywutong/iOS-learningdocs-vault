---
title: 'init(title:image:target:action:menu:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(title:image:target:action:menu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(title:image:target:action:menu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28title%3Aimage%3Atarget%3Aaction%3Amenu%3A%29.json'
content_hash: 'sha256:bfd9e164fea1b4d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(title:image:target:action:menu:)

<sub>Initializer</sub>

Creates a plain-style item using the specified title, image, target, action, and context menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(title: String?, image: UIImage?, target: AnyObject?, action: Selector?, menu: UIMenu? = nil)
```

## Parameters

- `title` — The item’s title. If `nil`, a title doesn’t appear.

- `image` — The item’s image. If `nil`, an image doesn’t appear. The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.

- `target` — The object that receives the `action` message.

- `action` — The action to send to `target` when a person selects this item.

- `menu` — The menu to present. The context menu displays in response to a person tapping the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating items

- [init(title:image:primaryAction:menu:)](<init(title_image_primaryaction_menu_).md>) — Creates a plain-style item using the specified title, image, primary action, and context menu.
- [- init](<init().md>) — Initializes the item to its default state.
- [- initWithCoder:](<init(coder_).md>) — Creates an item from data in an unarchiver.
