---
title: containerView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/containerview
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/containerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/containerview.json'
content_hash: 'sha256:080aac8e1770c8f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# containerView

<sub>Instance Property</sub>

The view in which the presentation occurs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var containerView: UIView? { get }
```

## Discussion

UIKit sets the value of this property shortly after receiving the presentation controller from your transitioning delegate. The container view is always an ancestor of the presented view controller’s view. During transition animations, the container view also contains the presenting view controller’s view. When adding custom views to a presentation, add them to the container view.

If your transition also employs custom animator objects, those objects can get this container view from the [containerView](../uiviewcontrollercontexttransitioning/containerview.md) property of the context object provided by UIKit.

## See Also

### Getting the presentation objects

- [presentingViewController](presentingviewcontroller.md) — The view controller that is the starting point for the presentation.
- [presentedViewController](presentedviewcontroller.md) — The view controller being presented.
- [presentedView](presentedview.md) — The view to be animated by the animator objects during a transition.
