---
title: 'tabBarController(_:didEndCustomizing:changed:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:didendcustomizing:changed:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:didendcustomizing:changed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Adidendcustomizing%3Achanged%3A%29.json'
content_hash: 'sha256:b5688c37774d0f96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:didEndCustomizing:changed:)

<sub>Instance Method</sub>

Tells the delegate that the tab bar customization sheet was dismissed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, didEndCustomizing viewControllers: [UIViewController], changed: Bool)
```

## Parameters

- `tabBarController` — The tab bar controller that is being customized.

- `viewControllers` — The view controllers of the tab bar controller. The arrangement of the controllers in the array represents the new display order within the tab bar.

- `changed` — A Boolean value indicating whether items changed on the tab bar. [true](../../swift/true.md) if items changed or [false](../../swift/false.md) if they did not.

## Discussion

You can use this method to respond to changes to the order of tabs in the tab bar.

## See Also

### Managing tab bar customizations

- [- tabBarController:willBeginCustomizingViewControllers:](<tabbarcontroller(__willbegincustomizing_).md>) — Tells the delegate that the tab bar customization sheet is about to be displayed.
- [- tabBarController:willEndCustomizingViewControllers:changed:](<tabbarcontroller(__willendcustomizing_changed_).md>) — Tells the delegate that the tab bar customization sheet is about to be dismissed.
