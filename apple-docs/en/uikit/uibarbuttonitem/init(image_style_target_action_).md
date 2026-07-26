---
title: 'init(image:style:target:action:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(image:style:target:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(image:style:target:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28image%3Astyle%3Atarget%3Aaction%3A%29.json'
content_hash: 'sha256:79fa4afb759a65b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(image:style:target:action:)

<sub>Initializer</sub>

Creates an item using the specified image, style, target, and action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(image: UIImage?, style: UIBarButtonItem.Style, target: Any?, action: Selector?)
```

## Parameters

- `image` — The item’s image. If `nil`, an image doesn’t appear. The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.

- `style` — The style of the item. For possible values, see [Style](style-swift.enum.md).

- `target` — The object that receives the `action` message.

- `action` — The action to send to `target` when a person selects this item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## See Also

### Related Documentation

- [- initWithBarButtonSystemItem:target:action:](<init(barbuttonsystemitem_target_action_).md>) — Creates an item using the specified system item, target, and action.

### Creating items of a specific style

- [- initWithTitle:style:target:action:](<init(title_style_target_action_).md>) — Creates an item using the specified title, style, target, and action.
- [- initWithImage:landscapeImagePhone:style:target:action:](<init(image_landscapeimagephone_style_target_action_).md>) — Creates an item using the specified images, style, target, and action.
