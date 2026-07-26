---
title: selectedViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/selectedviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/selectedviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/selectedviewcontroller.json'
content_hash: 'sha256:5ba3721a9c56bdbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# selectedViewController

<sub>Instance Property</sub>

The view controller associated with the currently selected tab item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
unowned(unsafe) var selectedViewController: UIViewController? { get set }
```

## Discussion

This view controller is the one whose custom view is currently displayed by the tab bar interface. The specified view controller must be in the [viewControllers](viewcontrollers.md) array. Assigning a new view controller to this property changes the currently displayed view and also selects an appropriate tab in the tab bar. Changing the view controller also updates the [selectedIndex](selectedindex.md) property accordingly. The default value of this property is `nil`.

In iOS 3.0 and later, you can use this property to select any of the view controllers in the [viewControllers](viewcontrollers.md) property. This includes view controllers that are managed by the More navigation controller and whose tab bar items are not visible in the tab bar. You can also use it to select the More navigation controller itself, which is available from the [moreNavigationController](morenavigationcontroller.md) property. Prior to iOS 3.0, you could select only the More navigation controller and the subset of view controllers whose tab bar item was visible. Attempting to set this property to a view controller whose tab bar item was not visible had no effect.

> [!note] Note
> The More interface is not available in tvOS.

## See Also

### Managing the selected tab

- [selectedTab](selectedtab.md) — The currently selected tab, which can be a root tab or any of their descendants.
- [selectedIndex](selectedindex.md) — The index of the view controller associated with the currently selected tab item.
