---
title: presentedView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/presentedview
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentedview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/presentedview.json'
content_hash: 'sha256:58ff0e15d4bb99c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# presentedView

<sub>Instance Property</sub>

The view to be animated by the animator objects during a transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var presentedView: UIView? { get }
```

## Return Value

The view to present. This view must be either the presented view controller’s view or an ancestor of that view.

## Discussion

The default implementation of this method returns the presented view controller’s view. If you want to animate a different view, you may override this method and return that view. The view you specify must either be the presented view controller’s view or must be one of its ancestors.

The view returned by this method is given to the animator objects, which are responsible for animating it onscreen. The animator objects retrieve the view using the [- viewForKey:](<../uiviewcontrollercontexttransitioning/view(forkey_).md>) method of the context object provided by UIKit.

UIKit calls this method multiple times during the course of a presentation, so your implementation should return the appropriate view as quickly as possible. Do not use this method to actually configure your view hierarchy. If you intend to return a custom view, configure your view hierarchy in the [- presentationTransitionWillBegin](<presentationtransitionwillbegin().md>) method.

## See Also

### Getting the presentation objects

- [presentingViewController](presentingviewcontroller.md) — The view controller that is the starting point for the presentation.
- [presentedViewController](presentedviewcontroller.md) — The view controller being presented.
- [containerView](containerview.md) — The view in which the presentation occurs.
