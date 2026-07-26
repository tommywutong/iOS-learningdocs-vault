---
title: 'tabBarController(_:tab:acceptItemsFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:tab:acceptitemsfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:tab:acceptitemsfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Atab%3Aacceptitemsfrom%3A%29.json'
content_hash: 'sha256:52eac7bb6862ca86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:tab:acceptItemsFrom:)

<sub>Instance Method</sub>

Notifies the delegate to perform a drop into the specified @c tab from the specified session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, tab: UITab, acceptItemsFrom session: any UIDropSession)
```

## Discussion

This is only called if the operation returned from `tabBarController:tab:operationForAcceptingItemsFromDropSession` is valid for a drop.
