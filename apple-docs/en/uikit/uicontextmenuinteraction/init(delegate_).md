---
title: 'init(delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuinteraction/init(delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteraction/init(delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteraction/init%28delegate%3A%29.json'
content_hash: 'sha256:60038a495ce665eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteraction](../uicontextmenuinteraction.md)

# init(delegate:)

<sub>Initializer</sub>

Creates a context menu interaction object with the specified delegate object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(delegate: any UIContextMenuInteractionDelegate)
```

## Parameters

- `delegate` — The object that provides the contextual menu and responds to other interaction-related events. This object must adopt the [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md) protocol.

## Return Value

A new context menu interaction object with the associated delegate.

## See Also

### Creating a context menu interaction object

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
