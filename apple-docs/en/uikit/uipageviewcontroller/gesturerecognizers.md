---
title: gestureRecognizers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/gesturerecognizers
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/gesturerecognizers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/gesturerecognizers.json'
content_hash: 'sha256:5d2c72d108296a74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# gestureRecognizers

<sub>Instance Property</sub>

An array of [UIGestureRecognizer](../uigesturerecognizer.md) objects that are configured to handle user interaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var gestureRecognizers: [UIGestureRecognizer] { get }
```

## Discussion

These gesture recognizers are initially attached to a view in the page view controller’s hierarchy. To change the region of the screen in which the user can navigate using gestures,  they can be placed on another view.

## See Also

### Providing Content

- [- setViewControllers:direction:animated:completion:](<setviewcontrollers(__direction_animated_completion_).md>) — Sets the view controllers to be displayed.
- [NavigationDirection](navigationdirection.md) — Directions for page-turn transitions.
- [viewControllers](viewcontrollers.md) — The view controllers displayed by the page view controller.
