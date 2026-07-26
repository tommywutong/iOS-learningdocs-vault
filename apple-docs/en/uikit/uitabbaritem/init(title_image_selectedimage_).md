---
title: 'init(title:image:selectedImage:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritem/init(title:image:selectedimage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/init(title:image:selectedimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/init%28title%3Aimage%3Aselectedimage%3A%29.json'
content_hash: 'sha256:bc094808687708a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# init(title:image:selectedImage:)

<sub>Initializer</sub>

Creates a tab bar item that toggles the image it displays when its selected state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(title: String?, image: UIImage?, selectedImage: UIImage?)
```

## Parameters

- `title` — The item’s title.

- `image` — The item’s source image.

- `selectedImage` — The source image the item uses when the user selects it.

## Discussion

Use `nil` for `title` or `image` if you don’t want to display that element.

If you don’t provide `selectedImage`, the item uses `image` for both selection states. The item creates the images it displays from the alpha values in the source images. To prevent system tinting, use images with the [UIImageRenderingModeAlwaysOriginal](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) rendering mode. The item clips any image that’s larger than its bounds.

## See Also

### Creating a tab bar item

- [- initWithTabBarSystemItem:tag:](<init(tabbarsystemitem_tag_).md>) — Creates a tab bar item using a system-provided configuration.
- [- initWithTitle:image:tag:](<init(title_image_tag_).md>) — Creates a tab bar item that displays a title and an image.
- [- init](<init().md>) — Creates a tab bar item with a default configuration.
- [- initWithCoder:](<init(coder_).md>) — Creates a tab bar item from a serialized instance.
- [SystemItem](systemitem.md) — Constants that represent the system tab bar items.
