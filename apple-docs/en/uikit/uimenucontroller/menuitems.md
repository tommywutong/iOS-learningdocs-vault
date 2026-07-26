---
title: menuItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenucontroller/menuitems
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/menuitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/menuitems.json'
content_hash: 'sha256:a06d54067a05a072'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# menuItems

<sub>Instance Property</sub>

The custom menu items for the editing menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var menuItems: [UIMenuItem]? { get set }
```

## Discussion

The default value is `nil` (no custom menu items). Each menu item is an instance of the UIMenuItem class. You may create your own menu items, each with its own title and action selector, and add them to the editing menu through this property. Custom items appear in the menu after any system menu items.
