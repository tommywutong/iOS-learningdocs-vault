---
title: 'pageViewController(_:willTransitionTo:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:willtransitionto:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:willtransitionto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller%28_%3Awilltransitionto%3A%29.json'
content_hash: 'sha256:6164dcef6d655b74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewControllerDelegate](../uipageviewcontrollerdelegate.md)

# pageViewController(_:willTransitionTo:)

<sub>Instance Method</sub>

Called before a gesture-driven transition begins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func pageViewController(_ pageViewController: UIPageViewController, willTransitionTo pendingViewControllers: [UIViewController])
```

## Parameters

- `pageViewController` — The page view controller.

- `pendingViewControllers` — The view controllers that are being transitioned to.

## Discussion

If the user aborts the navigation gesture, the transition doesn’t complete and the view controllers stay the same.

## See Also

### Responding to Page View Controller Events

- [- pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:](<pageviewcontroller(__didfinishanimating_previousviewcontrollers_transitioncompleted_).md>) — Called after a gesture-driven transition completes.
- [- pageViewController:spineLocationForInterfaceOrientation:](<pageviewcontroller(__spinelocationfor_).md>) — Returns the spine location for the given orientation.
