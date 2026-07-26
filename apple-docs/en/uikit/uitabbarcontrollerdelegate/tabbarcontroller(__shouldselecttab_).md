---
title: 'tabBarController(_:shouldSelectTab:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:shouldselecttab:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:shouldselecttab:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Ashouldselecttab%3A%29.json'
content_hash: 'sha256:b408b5c53185b511'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:shouldSelectTab:)

<sub>Instance Method</sub>

Asks the delegate whether the specified tab should be made active.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, shouldSelectTab tab: UITab) -> Bool
```

## Discussion

Return @c YES if the specified @c tab can be selected by the user. Otherwise, return @c NO
