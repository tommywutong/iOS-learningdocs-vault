---
title: tabBarController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/tabbarcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/tabbarcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/tabbarcontroller.json'
content_hash: 'sha256:b30fc1ac114aa969'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# tabBarController

<sub>Instance Property</sub>

The nearest ancestor in the view controller hierarchy that is a tab bar controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tabBarController: UITabBarController? { get }
```

## Discussion

If the view controller or one of its ancestors is a child of a tab bar controller, this property contains the owning tab bar controller. This property is `nil` if the view controller is not embedded inside a tab bar controller.

## See Also

### Getting other related view controllers

- [presentingViewController](presentingviewcontroller.md) — The view controller that presented this view controller.
- [presentedViewController](presentedviewcontroller.md) — The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [parentViewController](parent.md) — The parent view controller of the recipient.
- [splitViewController](splitviewcontroller.md) — The nearest ancestor in the view controller hierarchy that is a split view controller.
- [navigationController](navigationcontroller.md) — The nearest ancestor in the view controller hierarchy that is a navigation controller.
