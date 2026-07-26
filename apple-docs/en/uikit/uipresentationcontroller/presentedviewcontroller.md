---
title: presentedViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/presentedviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentedviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/presentedviewcontroller.json'
content_hash: 'sha256:d2c234c0fd99d52b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# presentedViewController

<sub>Instance Property</sub>

The view controller being presented.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var presentedViewController: UIViewController { get }
```

## Discussion

This object corresponds to the one passed as the first parameter of the [- presentViewController:animated:completion:](<../uiviewcontroller/present(__animated_completion_).md>) method. The successful conclusion of the presentation process causes this view controller’s content to be displayed onscreen.

## See Also

### Getting the presentation objects

- [presentingViewController](presentingviewcontroller.md) — The view controller that is the starting point for the presentation.
- [containerView](containerview.md) — The view in which the presentation occurs.
- [presentedView](presentedview.md) — The view to be animated by the animator objects during a transition.
