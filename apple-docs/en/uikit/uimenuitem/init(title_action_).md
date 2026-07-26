---
title: 'init(title:action:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uimenuitem/init(title:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenuitem/init(title:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuitem/init%28title%3Aaction%3A%29.json'
content_hash: 'sha256:f29747217fe954ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuItem](../uimenuitem.md)

# init(title:action:)

<sub>Initializer</sub>

Creates and returns a menu-item object initialized with the given title and action.

> [!warning] Deprecated
> For more information, see [UIMenuItem](../uimenuitem.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(title: String, action: Selector)
```

## Parameters

- `title` — The title of the menu item.

- `action` — A selector identifying the method of the responder object to invoke for handling the command represented by the menu item.

## Return Value

An initialized `UIMenuItem` object, or `nil` if there was a problem creating the object.
