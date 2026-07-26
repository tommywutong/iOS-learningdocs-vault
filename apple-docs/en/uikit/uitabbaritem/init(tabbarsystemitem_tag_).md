---
title: 'init(tabBarSystemItem:tag:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbaritem/init(tabbarsystemitem:tag:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbaritem/init(tabbarsystemitem:tag:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbaritem/init%28tabbarsystemitem%3Atag%3A%29.json'
content_hash: 'sha256:1289bed177ea6af2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarItem](../uitabbaritem.md)

# init(tabBarSystemItem:tag:)

<sub>Initializer</sub>

Creates a tab bar item using a system-provided configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(tabBarSystemItem systemItem: UITabBarItem.SystemItem, tag: Int)
```

## Parameters

- `systemItem` — The preferred system item. For possible values, see [SystemItem](systemitem.md).

- `tag` — An integer you use to identify the object.

## Discussion

You can’t change the [title](../uibaritem/title.md) and [image](../uibaritem/image.md) properties of an item this method creates.

## See Also

### Creating a tab bar item

- [- initWithTitle:image:tag:](<init(title_image_tag_).md>) — Creates a tab bar item that displays a title and an image.
- [- initWithTitle:image:selectedImage:](<init(title_image_selectedimage_).md>) — Creates a tab bar item that toggles the image it displays when its selected state changes.
- [- init](<init().md>) — Creates a tab bar item with a default configuration.
- [- initWithCoder:](<init(coder_).md>) — Creates a tab bar item from a serialized instance.
- [SystemItem](systemitem.md) — Constants that represent the system tab bar items.
