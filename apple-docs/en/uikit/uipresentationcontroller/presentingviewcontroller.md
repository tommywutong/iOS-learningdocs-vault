---
title: presentingViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/presentingviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentingviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/presentingviewcontroller.json'
content_hash: 'sha256:60834d987dcd21d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# presentingViewController

<sub>Instance Property</sub>

The view controller that is the starting point for the presentation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var presentingViewController: UIViewController { get }
```

## Discussion

The object in this property could be the root view controller of the window, a parent view controller that is marked as defining the current context, or the last view controller that was presented onscreen. This view controller may or may not be the same one whose [- presentViewController:animated:completion:](<../uiviewcontroller/present(__animated_completion_).md>) method was called to initiate the presentation process. It may also not be the view controller used to initialize your presentation controller.

## See Also

### Getting the presentation objects

- [presentedViewController](presentedviewcontroller.md) — The view controller being presented.
- [containerView](containerview.md) — The view in which the presentation occurs.
- [presentedView](presentedview.md) — The view to be animated by the animator objects during a transition.
