---
title: 'init(style:title:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextualaction/init(style:title:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextualaction/init(style:title:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextualaction/init%28style%3Atitle%3Ahandler%3A%29.json'
content_hash: 'sha256:359c0f24546713ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextualAction](../uicontextualaction.md)

# init(style:title:handler:)

<sub>Initializer</sub>

Creates a new contextual action with the specified title and handler.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(style: UIContextualAction.Style, title: String?, handler: @escaping UIContextualAction.Handler)
```

## Parameters

- `style` — The style information to apply to the action button.

- `title` — The title of the action button.

- `handler` — The handler to execute when the user selects the action.

## Return Value

An initialized contextual action object.
