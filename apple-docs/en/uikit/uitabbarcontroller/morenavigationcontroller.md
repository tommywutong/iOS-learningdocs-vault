---
title: moreNavigationController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/morenavigationcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/morenavigationcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/morenavigationcontroller.json'
content_hash: 'sha256:cb70fe5785bb7d17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# moreNavigationController

<sub>Instance Property</sub>

The view controller that manages the More navigation interface.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var moreNavigationController: UINavigationController { get }
```

## Discussion

This property always contains a valid More navigation controller, even if a More button is not displayed on the screen. You can use the value of this property to select the More navigation controller in the tab bar interface or to compare it against the currently selected view controller.

Do not add the object stored in this property to your tab bar interface manually. The More controller is displayed automatically by the tab bar controller as it is needed. You must also not look for the More navigation controller in the array of view controllers stored in the [viewControllers](viewcontrollers.md) property. The tab bar controller does not include the More navigation controller in that array of objects.

> [!note] Note
> The More interface is not available in tvOS.

## See Also

### Managing the view controllers

- [viewControllers](viewcontrollers.md) — An array of the root view controllers displayed by the tab bar interface.
- [- setViewControllers:animated:](<setviewcontrollers(__animated_).md>) — Sets the root view controllers of the tab bar controller.
- [customizableViewControllers](customizableviewcontrollers.md) — The subset of view controllers managed by this tab bar controller that can be customized.
