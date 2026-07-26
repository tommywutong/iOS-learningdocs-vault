---
title: UIContextMenuContentPreviewProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenucontentpreviewprovider
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenucontentpreviewprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenucontentpreviewprovider.json'
content_hash: 'sha256:41a88c13edf5fa63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextMenuContentPreviewProvider

<sub>Type Alias</sub>

Returns the custom view controller to use when previewing your content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UIContextMenuContentPreviewProvider = () -> UIViewController?
```

## Return Value

The view controller to display in place of the system’s standard view controller. If you want UIKit to present your content using a default view controller, return `nil`.

## Discussion

Use this handler to load or create your custom view controller, configure it with your content, and return it to UIKit.

## See Also

### Creating the menu configuration object

- [init(identifier:previewProvider:actionProvider:)](<uicontextmenuconfiguration/init(identifier_previewprovider_actionprovider_).md>) — Creates a menu configuration object with the specified action and preview providers.
- [UIContextMenuActionProvider](uicontextmenuactionprovider.md) — Returns an action-based contextual menu, optionally incorporating the system-suggested actions.
