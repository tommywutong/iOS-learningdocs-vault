---
title: 'view(forKey:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollercontexttransitioning/view(forkey:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/view(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/view%28forkey%3A%29.json'
content_hash: 'sha256:92245db6e3ef2980'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# view(forKey:)

<sub>Instance Method</sub>

Returns the specified view involved in the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func view(forKey key: UITransitionContextViewKey) -> UIView?
```

## Parameters

- `key` — The key identifying the view you want. For a list of possible keys, see `View Transition Keys`.

## Return Value

The view object for the specified key or `nil` if the view could not be found.

## Discussion

The view returned by this method may or may not be the root view of the corresponding view controller. A situation where the views may not be the same is when a system-provided presentation controller installs another view underneath the presented view controller’s view.

## See Also

### Accessing the transition objects

- [containerView](containerview.md) — The view that acts as the superview for the views involved in the transition.
- [- viewControllerForKey:](<viewcontroller(forkey_).md>) — Returns a view controller involved in the transition.
