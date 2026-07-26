---
title: preferredTransition
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/preferredtransition
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferredtransition.json'
content_hash: 'sha256:57a1a009615780d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# preferredTransition

<sub>Instance Property</sub>

An object that defines the transition animation when switching to the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredTransition: UIViewController.Transition? { get set }
```

## Discussion

Use this property to define which transition the system uses when you present a view controller. For more information, see [Enhancing your app with fluid transitions](../enhancing-your-app-with-fluid-transitions.md).

## See Also

### Working with transitions

- [Transition](transition.md) — An object that defines the transition animation when switching to a new view controller.
