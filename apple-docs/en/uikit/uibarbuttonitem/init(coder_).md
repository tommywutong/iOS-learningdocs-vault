---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28coder%3A%29.json'
content_hash: 'sha256:3391db3272d5368d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(coder:)

<sub>Initializer</sub>

Creates an item from data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — An unarchiver object.

## See Also

### Creating items

- [init(title:image:primaryAction:menu:)](<init(title_image_primaryaction_menu_).md>) — Creates a plain-style item using the specified title, image, primary action, and context menu.
- [init(title:image:target:action:menu:)](<init(title_image_target_action_menu_).md>) — Creates a plain-style item using the specified title, image, target, action, and context menu.
- [- init](<init().md>) — Initializes the item to its default state.
