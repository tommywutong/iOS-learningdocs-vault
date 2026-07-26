---
title: presentedViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/presentedviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/presentedviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/presentedviewcontroller.json'
content_hash: 'sha256:3f6b6bed59f0f9a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# presentedViewController

<sub>Instance Property</sub>

The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var presentedViewController: UIViewController? { get }
```

## Discussion

When you present a view controller modally (either explicitly or implicitly) using the [- presentViewController:animated:completion:](<present(__animated_completion_).md>) method, the view controller that called the method has this property set to the view controller that it presented. If the current view controller did not present another view controller modally, the value in this property is `nil`.

## See Also

### Getting other related view controllers

- [presentingViewController](presentingviewcontroller.md) — The view controller that presented this view controller.
- [parentViewController](parent.md) — The parent view controller of the recipient.
- [splitViewController](splitviewcontroller.md) — The nearest ancestor in the view controller hierarchy that is a split view controller.
- [navigationController](navigationcontroller.md) — The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [tabBarController](tabbarcontroller.md) — The nearest ancestor in the view controller hierarchy that is a tab bar controller.
