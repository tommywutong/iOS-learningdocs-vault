---
title: UIContextMenuActionProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuactionprovider
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuactionprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuactionprovider.json'
content_hash: 'sha256:1bc1e8a987c86e29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextMenuActionProvider

<sub>Type Alias</sub>

Returns an action-based contextual menu, optionally incorporating the system-suggested actions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UIContextMenuActionProvider = ([UIMenuElement]) -> UIMenu?
```

## Parameters

- `suggestedActions` — Suggested actions for you to include in your menu. UIKit collects these actions from responders in the current responder chain. You are not required to include the actions in your menu.

## Return Value

The menu object containing the actions for the user to select.

## Discussion

Use this handler to create [UIAction](uiaction.md) objects representing the actions the user may choose from your menu. To organize groups of actions hierarchically, create a [UIMenu](uimenu.md) object to represent a submenu and add nested actions to it. Finally, build your top-level [UIMenu](uimenu.md) object from the actions and submenus you created, and return that menu object from your handler.

## See Also

### Creating the menu configuration object

- [init(identifier:previewProvider:actionProvider:)](<uicontextmenuconfiguration/init(identifier_previewprovider_actionprovider_).md>) — Creates a menu configuration object with the specified action and preview providers.
- [UIContextMenuContentPreviewProvider](uicontextmenucontentpreviewprovider.md) — Returns the custom view controller to use when previewing your content.
