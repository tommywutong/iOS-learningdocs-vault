---
title: 'viewController(forKey:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollercontexttransitioning/viewcontroller(forkey:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/viewcontroller(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/viewcontroller%28forkey%3A%29.json'
content_hash: 'sha256:07a95b1fe63fd5a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# viewController(forKey:)

<sub>Instance Method</sub>

Returns a view controller involved in the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewController(forKey key: UITransitionContextViewControllerKey) -> UIViewController?
```

## Parameters

- `key` — The key identifying the view controller you want. For a list of possible keys, see `View Controller Transition Keys`.

## Return Value

The view controller object for the specified key or `nil` if the view controller could not be found.

## See Also

### Accessing the transition objects

- [containerView](containerview.md) — The view that acts as the superview for the views involved in the transition.
- [- viewForKey:](<view(forkey_).md>) — Returns the specified view involved in the transition.
