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
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/containerview
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/containerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/containerview.json'
content_hash: 'sha256:bbf66ffc95250611'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# containerView

<sub>Instance Property</sub>

Returns the view in which the transition takes place.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var containerView: UIView { get }
```

## Return Value

The container view for the transition animation.

## Discussion

The container view acts as the host view for any animations between the transitioning view controllers. When animating your own custom views, add them to the container view if you want them to interoperate with the view controllers’ views.

## See Also

### Getting the views and view controllers

- [- viewControllerForKey:](<viewcontroller(forkey_).md>) — Returns the view controllers involved in the transition.
- [- viewForKey:](<view(forkey_).md>) — Returns the specified view involved in the transition.
