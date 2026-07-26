---
title: 'tabBarController(_:didSelect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:didselect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:didselect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Adidselect%3A%29.json'
content_hash: 'sha256:8a14597f2ce0de54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:didSelect:)

<sub>Instance Method</sub>

Tells the delegate that the user selected an item in the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, didSelect viewController: UIViewController)
```

## Parameters

- `tabBarController` — The tab bar controller containing `viewController`.

- `viewController` — The view controller that the user selected. In iOS v3.0 and later, this could be the same view controller that was already selected.

## Discussion

In iOS v3.0 and later, the tab bar controller calls this method regardless of whether the selected view controller changed. In addition, it is called only in response to user taps in the tab bar and is not called when your code changes the tab bar contents programmatically.

In versions of iOS prior to version 3.0, this method is called only when the selected view controller actually changes. In other words, it is not called when the same view controller is selected. In addition, the method was called for both programmatic and user-initiated changes to the selected view controller.

## See Also

### Managing tab bar selections

- [- tabBarController:shouldSelectViewController:](<tabbarcontroller(__shouldselect_).md>) — Asks the delegate whether the specified view controller should be made active.
