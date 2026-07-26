---
title: viewControllers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/viewcontrollers
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/viewcontrollers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/viewcontrollers.json'
content_hash: 'sha256:74872f05e5f90f66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# viewControllers

<sub>Instance Property</sub>

The view controllers currently on the navigation stack.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var viewControllers: [UIViewController] { get set }
```

## Discussion

The root view controller is at index `0` in the array, the back view controller is at index `n-2`, and the top controller is at index `n-1`, where `n` is the number of items in the array.

Assigning a new array of view controllers to this property is equivalent to calling the [- setViewControllers:animated:](<setviewcontrollers(__animated_).md>) method with the `animated` parameter set to [false](../../swift/false.md).

## See Also

### Accessing items on the navigation stack

- [topViewController](topviewcontroller.md) — The view controller at the top of the navigation stack.
- [visibleViewController](visibleviewcontroller.md) — The view controller associated with the currently visible view in the navigation interface.
- [- setViewControllers:animated:](<setviewcontrollers(__animated_).md>) — Replaces the view controllers currently managed by the navigation controller with the specified items.
