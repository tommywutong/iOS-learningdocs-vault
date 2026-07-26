---
title: 'buildMenu(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/buildmenu(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/buildmenu(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/buildmenu%28with%3A%29.json'
content_hash: 'sha256:9e142f62614b8fa4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# buildMenu(with:)

<sub>Instance Method</sub>

Asks the receiving responder to add and remove items from a menu system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func buildMenu(with builder: any UIMenuBuilder)
```

## Parameters

- `builder` — An object that you use to modify a menu system for your app.

## Discussion

Override this method in your app delegate or view controller to receive a [UIMenuBuilder](../uimenubuilder.md) object. Use the builder to add and remove [UIMenuElement](../uimenuelement.md) objects such as [UIMenu](../uimenu.md), [UIAction](../uiaction.md), and [UICommand](../uicommand.md) from your app’s menu bar or context menus.

> [!note] Note
> The menu bar is available in Mac apps built with Mac Catalyst.

Where you override this method determines the menu system that the builder updates. To add and remove items from the menu bar using the [mainSystem](../uimenusystem/main.md) menu system, override [- buildMenuWithBuilder:](<buildmenu(with_).md>) in your app delegate. To build a [contextSystem](../uimenusystem/context.md) menu using the context system, override this method in your view controller.

## See Also

### Building and validating commands

- [- validateCommand:](<validate(__).md>) — Asks the receiving responder to validate the command.
- [- canPerformAction:withSender:](<canperformaction(__withsender_).md>) — Requests the receiving responder to enable or disable the specified command in the user interface.
- [- targetForAction:withSender:](<target(foraction_withsender_).md>) — Returns the target object that responds to an action.
