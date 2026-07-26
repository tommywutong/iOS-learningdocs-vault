---
title: toolbarItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/toolbaritems
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/toolbaritems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/toolbaritems.json'
content_hash: 'sha256:898d095cd23b6258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# toolbarItems

<sub>Instance Property</sub>

The toolbar items associated with the view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var toolbarItems: [UIBarButtonItem]? { get set }
```

## Discussion

This property contains an array of [UIBarButtonItem](../uibarbuttonitem.md) objects and works in conjunction with a [UINavigationController](../uinavigationcontroller.md) object. If this view controller is embedded inside a navigation controller interface, and the navigation controller displays a toolbar, this property identifies the items to display in that toolbar.

You can set the value of this property explicitly or use the [- setToolbarItems:animated:](<settoolbaritems(__animated_).md>) method to animate changes to the visible set of toolbar items.

## See Also

### Configuring a navigation interface

- [navigationItem](navigationitem.md) — The navigation item used to represent the view controller in a parent’s navigation bar.
- [hidesBottomBarWhenPushed](hidesbottombarwhenpushed.md) — A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.
- [- setToolbarItems:animated:](<settoolbaritems(__animated_).md>) — Sets the toolbar items to be displayed along with the view controller.
