---
title: containerView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning/containerview
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/containerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/containerview.json'
content_hash: 'sha256:db99ed32569a11d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# containerView

<sub>Instance Property</sub>

The view that acts as the superview for the views involved in the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var containerView: UIView { get }
```

## Return Value

The view that contains both views involved in the transition.

## Discussion

The container view acts as the superview of all other views (including those of the presenting and presented view controllers) during the animation sequence. UIKit sets this view for you and automatically adds the view of the presenting view controller to it. The animator object is responsible for adding the view of the presented view controller, and the animator object or presentation controller must use this view as the container for all other views involved in the transition.

## See Also

### Accessing the transition objects

- [- viewControllerForKey:](<viewcontroller(forkey_).md>) — Returns a view controller involved in the transition.
- [- viewForKey:](<view(forkey_).md>) — Returns the specified view involved in the transition.
