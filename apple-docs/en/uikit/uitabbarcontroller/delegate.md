---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/delegate.json'
content_hash: 'sha256:c138e361e1cc859c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# delegate

<sub>Instance Property</sub>

The tab bar controller’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UITabBarControllerDelegate)? { get set }
```

## Discussion

You can use the delegate object to track changes to the items in the tab bar and to monitor the selection of tabs. The delegate object you provide should conform to the [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md) protocol. The default value for this property is `nil`.

## See Also

### Customizing the tab bar behavior

- [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md) — A set of methods you implement to customize the behavior of a tab bar.
- [tabBarMinimizeBehavior](tabbarminimizebehavior.md) — Defines the minimize behavior for the tab bar, if it is supported.
- [MinimizeBehavior](minimizebehavior.md)
