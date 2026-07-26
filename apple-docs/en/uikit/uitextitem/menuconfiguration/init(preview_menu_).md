---
title: 'init(preview:menu:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextitem/menuconfiguration/init(preview:menu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextitem/menuconfiguration/init(preview:menu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextitem/menuconfiguration/init%28preview%3Amenu%3A%29.json'
content_hash: 'sha256:48a777ccbb4ca2d8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITextItem](../../uitextitem.md) · [MenuConfiguration](../menuconfiguration.md)

# init(preview:menu:)

<sub>Initializer</sub>

Creates a text item menu configuration with the specified menu and preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(preview: UITextItem.MenuConfiguration.Preview? = .default, menu: UIMenu)
```

## Parameters

- `preview` — The preview to display alongside the menu.

- `menu` — The menu to present when the user interacts with the text item.

## See Also

### Creating a menu configuration

- [Preview](preview.md) — Constants that indicate what type of preview to display alongside the text item’s menu.
