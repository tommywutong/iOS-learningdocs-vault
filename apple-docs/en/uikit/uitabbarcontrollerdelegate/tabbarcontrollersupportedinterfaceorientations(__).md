---
title: 'tabBarControllerSupportedInterfaceOrientations(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollersupportedinterfaceorientations(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollersupportedinterfaceorientations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollersupportedinterfaceorientations%28_%3A%29.json'
content_hash: 'sha256:6a0374d86b0cdce3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarControllerSupportedInterfaceOrientations(_:)

<sub>Instance Method</sub>

Called to allow the delegate to provide the complete set of supported interface orientations for the tab bar controller.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func tabBarControllerSupportedInterfaceOrientations(_ tabBarController: UITabBarController) -> UIInterfaceOrientationMask
```

## Parameters

- `tabBarController` — The tab bar controller that is asking the delegate object for the supported interface orientations.

## Return Value

One of the [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md) constants that represents the set of interface orientations supported by the tab bar controller.

## See Also

### Related Documentation

- [supportedInterfaceOrientations](../uiviewcontroller/supportedinterfaceorientations.md) — The interface orientations that the view controller supports.

### Overriding view rotation settings

- [- tabBarControllerPreferredInterfaceOrientationForPresentation:](<tabbarcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Called to allow the delegate to provide the preferred orientation for presentation of the tab bar controller.
