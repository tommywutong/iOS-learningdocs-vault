---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritem/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/init%28coder%3A%29.json'
content_hash: 'sha256:8745996bb186cb20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# init(coder:)

<sub>Initializer</sub>

Creates a tab bar item from a serialized instance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — The coder to use when deserializing the item.

## See Also

### Creating a tab bar item

- [- initWithTabBarSystemItem:tag:](<init(tabbarsystemitem_tag_).md>) — Creates a tab bar item using a system-provided configuration.
- [- initWithTitle:image:tag:](<init(title_image_tag_).md>) — Creates a tab bar item that displays a title and an image.
- [- initWithTitle:image:selectedImage:](<init(title_image_selectedimage_).md>) — Creates a tab bar item that toggles the image it displays when its selected state changes.
- [- init](<init().md>) — Creates a tab bar item with a default configuration.
- [SystemItem](systemitem.md) — Constants that represent the system tab bar items.
