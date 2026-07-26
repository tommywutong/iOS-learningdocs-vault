---
title: 'setToolbarItems(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/settoolbaritems(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/settoolbaritems(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/settoolbaritems%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:b37af3229596b4cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setToolbarItems(_:animated:)

<sub>Instance Method</sub>

Sets the toolbar items to be displayed along with the view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated: Bool)
```

## Parameters

- `toolbarItems` — The toolbar items to display in a built-in toolbar.

- `animated` — If [true](../../swift/true.md), animate the change of items in the toolbar.

## Discussion

View controllers that are managed by a navigation controller can use this method to specify toolbar items for the navigation controller’s built-in toolbar. You can set the toolbar items for your view controller before your view controller is displayed or after it is already visible.

## See Also

### Configuring a navigation interface

- [navigationItem](navigationitem.md) — The navigation item used to represent the view controller in a parent’s navigation bar.
- [hidesBottomBarWhenPushed](hidesbottombarwhenpushed.md) — A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.
- [toolbarItems](toolbaritems.md) — The toolbar items associated with the view controller.
