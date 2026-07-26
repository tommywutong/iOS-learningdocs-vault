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
doc_path: '/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/view(forkey:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/view(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/view%28forkey%3A%29.json'
content_hash: 'sha256:90509c5660309d16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# view(forKey:)

<sub>Instance Method</sub>

Returns the specified view involved in the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func view(forKey key: UITransitionContextViewKey) -> UIView?
```

## Parameters

- `key` — The key identifying the view you want. For a list of possible keys, see [UITransitionContextViewKey](../uitransitioncontextviewkey.md).

## Return Value

The view object for the specified key or `nil` if the view could not be found.

## See Also

### Getting the views and view controllers

- [- viewControllerForKey:](<viewcontroller(forkey_).md>) — Returns the view controllers involved in the transition.
- [containerView](containerview.md) — Returns the view in which the transition takes place.
