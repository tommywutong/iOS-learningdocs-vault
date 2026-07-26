---
title: 'tabBarController(_:willEndCustomizing:changed:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willendcustomizing:changed:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willendcustomizing:changed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Awillendcustomizing%3Achanged%3A%29.json'
content_hash: 'sha256:1626137035221a9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:willEndCustomizing:changed:)

<sub>Instance Method</sub>

Tells the delegate that the tab bar customization sheet is about to be dismissed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, willEndCustomizing viewControllers: [UIViewController], changed: Bool)
```

## Parameters

- `tabBarController` — The tab bar controller that is being customized.

- `viewControllers` — The view controllers of the tab bar controller. The arrangement of the controllers in the array represents the new display order within the tab bar.

- `changed` — A Boolean value indicating whether items changed on the tab bar. [true](../../swift/true.md) if items changed or [false](../../swift/false.md) if they did not.

## Discussion

This method is called in response to the user tapping the Done button on the sheet but before the sheet is dismissed.

## See Also

### Managing tab bar customizations

- [- tabBarController:willBeginCustomizingViewControllers:](<tabbarcontroller(__willbegincustomizing_).md>) — Tells the delegate that the tab bar customization sheet is about to be displayed.
- [- tabBarController:didEndCustomizingViewControllers:changed:](<tabbarcontroller(__didendcustomizing_changed_).md>) — Tells the delegate that the tab bar customization sheet was dismissed.
