---
title: visibleViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/visibleviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/visibleviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/visibleviewcontroller.json'
content_hash: 'sha256:f16379a59cea75b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# visibleViewController

<sub>Instance Property</sub>

The view controller associated with the currently visible view in the navigation interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var visibleViewController: UIViewController? { get }
```

## Discussion

The currently visible view can belong either to the view controller at the top of the navigation stack or to a view controller that was presented modally on top of the navigation controller itself.

## See Also

### Accessing items on the navigation stack

- [topViewController](topviewcontroller.md) — The view controller at the top of the navigation stack.
- [viewControllers](viewcontrollers.md) — The view controllers currently on the navigation stack.
- [- setViewControllers:animated:](<setviewcontrollers(__animated_).md>) — Replaces the view controllers currently managed by the navigation controller with the specified items.
