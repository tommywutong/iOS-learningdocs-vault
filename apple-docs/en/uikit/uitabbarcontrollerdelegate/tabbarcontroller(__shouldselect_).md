---
title: 'tabBarController(_:shouldSelect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:shouldselect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:shouldselect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Ashouldselect%3A%29.json'
content_hash: 'sha256:48713dd4bed5b264'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:shouldSelect:)

<sub>Instance Method</sub>

Asks the delegate whether the specified view controller should be made active.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, shouldSelect viewController: UIViewController) -> Bool
```

## Parameters

- `tabBarController` — The tab bar controller containing `viewController`.

- `viewController` — The view controller belonging to the tab that was tapped by the user.

## Return Value

[true](../../swift/true.md) if the view controller’s tab should be selected or [false](../../swift/false.md) if the current tab should remain active.

## Discussion

The tab bar controller calls this method in response to the user tapping a tab bar item. You can use this method to dynamically decide whether a given tab should be made the active tab.

## See Also

### Managing tab bar selections

- [- tabBarController:didSelectViewController:](<tabbarcontroller(__didselect_).md>) — Tells the delegate that the user selected an item in the tab bar.
