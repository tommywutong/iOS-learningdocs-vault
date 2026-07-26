---
title: 'tabBarController(_:willBeginCustomizing:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willbegincustomizing:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willbegincustomizing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Awillbegincustomizing%3A%29.json'
content_hash: 'sha256:5a7296fb25c3547a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:willBeginCustomizing:)

<sub>Instance Method</sub>

Tells the delegate that the tab bar customization sheet is about to be displayed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, willBeginCustomizing viewControllers: [UIViewController])
```

## Parameters

- `tabBarController` — The tab bar controller that is being customized.

- `viewControllers` — The view controllers to be displayed in the customization sheet. This list typically contains all custom view controllers you added but does not include some standard controllers, such as the one that manages the More tab.

## See Also

### Managing tab bar customizations

- [- tabBarController:willEndCustomizingViewControllers:changed:](<tabbarcontroller(__willendcustomizing_changed_).md>) — Tells the delegate that the tab bar customization sheet is about to be dismissed.
- [- tabBarController:didEndCustomizingViewControllers:changed:](<tabbarcontroller(__didendcustomizing_changed_).md>) — Tells the delegate that the tab bar customization sheet was dismissed.
