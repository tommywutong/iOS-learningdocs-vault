---
title: 'init(title:image:tag:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritem/init(title:image:tag:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/init(title:image:tag:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/init%28title%3Aimage%3Atag%3A%29.json'
content_hash: 'sha256:3b38eafb9c4da51b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# init(title:image:tag:)

<sub>Initializer</sub>

Creates a tab bar item that displays a title and an image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(title: String?, image: UIImage?, tag: Int)
```

## Parameters

- `title` — The item’s title.

- `image` — The item’s source image.

- `tag` — An integer you use to identify the object.

## Discussion

Use `nil` for `title` or `image` to not display that element.

By default, the item displays the same image regardless of its selected state. To display a different image for the selected state, set its [selectedImage](selectedimage.md) property. The item creates the images it displays from the alpha values in the source images. To prevent system tinting, use images with the [UIImageRenderingModeAlwaysOriginal](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) rendering mode. The item clips any image that’s larger than its bounds.

## See Also

### Creating a tab bar item

- [- initWithTabBarSystemItem:tag:](<init(tabbarsystemitem_tag_).md>) — Creates a tab bar item using a system-provided configuration.
- [- initWithTitle:image:selectedImage:](<init(title_image_selectedimage_).md>) — Creates a tab bar item that toggles the image it displays when its selected state changes.
- [- init](<init().md>) — Creates a tab bar item with a default configuration.
- [- initWithCoder:](<init(coder_).md>) — Creates a tab bar item from a serialized instance.
- [SystemItem](systemitem.md) — Constants that represent the system tab bar items.
