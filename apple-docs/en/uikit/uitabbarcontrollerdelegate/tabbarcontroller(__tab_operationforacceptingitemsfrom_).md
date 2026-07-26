---
title: 'tabBarController(_:tab:operationForAcceptingItemsFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:tab:operationforacceptingitemsfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:tab:operationforacceptingitemsfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Atab%3Aoperationforacceptingitemsfrom%3A%29.json'
content_hash: 'sha256:cb26c2f1e93b2334'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:tab:operationForAcceptingItemsFrom:)

<sub>Instance Method</sub>

Asks the delegate for a drop operation to determine if drag items can be dropped into the specified @c tab

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, tab: UITab, operationForAcceptingItemsFrom session: any UIDropSession) -> UIDropOperation
```

## Discussion

If the operation is either a `.move` or `.copy`, then the drop will proceed and `tabBarController:tab:acceptItemsFromDropSession:` is called. By default, the drop will be treated as a cancel operation if this is not implemented.
