---
title: 'init(image:landscapeImagePhone:style:target:action:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(image:landscapeimagephone:style:target:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(image:landscapeimagephone:style:target:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28image%3Alandscapeimagephone%3Astyle%3Atarget%3Aaction%3A%29.json'
content_hash: 'sha256:6350ffb59cb55159'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(image:landscapeImagePhone:style:target:action:)

<sub>Initializer</sub>

Creates an item using the specified images, style, target, and action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(image: UIImage?, landscapeImagePhone: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)
```

## Parameters

- `image` — The item’s image. If `nil`, an image doesn’t appear.

- `landscapeImagePhone` — The image to use for the item in landscape bars in the [UIUserInterfaceIdiomPhone](../uiuserinterfaceidiom/phone.md) idiom.

- `style` — The style of the item. For possible values, see [Style](style-swift.enum.md).

- `target` — The object that receives the `action` message.

- `action` — The action to send to `target` when a person selects this item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Creating items of a specific style

- [- initWithTitle:style:target:action:](<init(title_style_target_action_).md>) — Creates an item using the specified title, style, target, and action.
- [- initWithImage:style:target:action:](<init(image_style_target_action_).md>) — Creates an item using the specified image, style, target, and action.
