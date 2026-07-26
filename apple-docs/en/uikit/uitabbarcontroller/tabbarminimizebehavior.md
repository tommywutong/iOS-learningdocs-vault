---
title: tabBarMinimizeBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/tabbarminimizebehavior
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/tabbarminimizebehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/tabbarminimizebehavior.json'
content_hash: 'sha256:20092d346adde84b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# tabBarMinimizeBehavior

<sub>Instance Property</sub>

Defines the minimize behavior for the tab bar, if it is supported.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tabBarMinimizeBehavior: UITabBarController.MinimizeBehavior { get set }
```

## Discussion

The default value for this property is `UITabBarMinimizeBehaviorAutomatic`.

## See Also

### Customizing the tab bar behavior

- [delegate](delegate.md) — The tab bar controller’s delegate object.
- [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md) — A set of methods you implement to customize the behavior of a tab bar.
- [MinimizeBehavior](minimizebehavior.md)
