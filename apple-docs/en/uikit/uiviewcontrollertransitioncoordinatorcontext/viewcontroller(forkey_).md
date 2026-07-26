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
doc_path: '/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/viewcontroller(forkey:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/viewcontroller(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/viewcontroller%28forkey%3A%29.json'
content_hash: 'sha256:16d64978042fe49f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# viewController(forKey:)

<sub>Instance Method</sub>

Returns the view controllers involved in the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewController(forKey key: UITransitionContextViewControllerKey) -> UIViewController?
```

## Parameters

- `key` — The key indicating which view controller you want. For a list of possible values, see [UITransitionContextViewControllerKey](../uitransitioncontextviewcontrollerkey.md).

## Return Value

The view controller associated with the key.

## Discussion

The view controller associated with the [UITransitionContextFromViewControllerKey](../uitransitioncontextviewcontrollerkey/from.md) key corresponds to the view controller that’s already onscreen. The view controller associated with the [UITransitionContextToViewControllerKey](../uitransitioncontextviewcontrollerkey/to.md) key corresponds to the view controller that’s to be animated onscreen.

## See Also

### Getting the views and view controllers

- [- viewForKey:](<view(forkey_).md>) — Returns the specified view involved in the transition.
- [containerView](containerview.md) — Returns the view in which the transition takes place.
