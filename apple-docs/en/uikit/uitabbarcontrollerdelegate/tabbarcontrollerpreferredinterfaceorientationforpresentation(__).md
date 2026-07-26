---
title: 'tabBarControllerPreferredInterfaceOrientationForPresentation(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation%28_%3A%29.json'
content_hash: 'sha256:19c85675bd0fd570'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarControllerPreferredInterfaceOrientationForPresentation(_:)

<sub>Instance Method</sub>

Called to allow the delegate to provide the preferred orientation for presentation of the tab bar controller.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func tabBarControllerPreferredInterfaceOrientationForPresentation(_ tabBarController: UITabBarController) -> UIInterfaceOrientation
```

## Parameters

- `tabBarController` — The tab bar controller that is asking the delegate object for the preferred presentation orientation.

## Return Value

The preferred orientation for presenting the tab bar controller.

## See Also

### Related Documentation

- [preferredInterfaceOrientationForPresentation](../uiviewcontroller/preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.

### Overriding view rotation settings

- [- tabBarControllerSupportedInterfaceOrientations:](<tabbarcontrollersupportedinterfaceorientations(__).md>) — Called to allow the delegate to provide the complete set of supported interface orientations for the tab bar controller.
