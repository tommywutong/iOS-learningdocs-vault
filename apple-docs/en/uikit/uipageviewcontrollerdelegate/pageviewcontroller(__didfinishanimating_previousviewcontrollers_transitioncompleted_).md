---
title: 'pageViewController(_:didFinishAnimating:previousViewControllers:transitionCompleted:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:didfinishanimating:previousviewcontrollers:transitioncompleted:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:didfinishanimating:previousviewcontrollers:transitioncompleted:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller%28_%3Adidfinishanimating%3Apreviousviewcontrollers%3Atransitioncompleted%3A%29.json'
content_hash: 'sha256:55619e953ff41ee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewControllerDelegate](../uipageviewcontrollerdelegate.md)

# pageViewController(_:didFinishAnimating:previousViewControllers:transitionCompleted:)

<sub>Instance Method</sub>

Called after a gesture-driven transition completes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func pageViewController(_ pageViewController: UIPageViewController, didFinishAnimating finished: Bool, previousViewControllers: [UIViewController], transitionCompleted completed: Bool)
```

## Parameters

- `pageViewController` — The page view controller.

- `finished` — [true](../../swift/true.md) if the animation finished; otherwise, [false](../../swift/false.md).

- `previousViewControllers` — The view controllers prior to the transition.

- `completed` — [true](../../swift/true.md) if the user completed the page-turn gesture; otherwise, [false](../../swift/false.md).

## Discussion

Use the `completed` parameter to distinguish between a transition that completed (the page was turned) and a transition that the user aborted (the page was not turned).

The value of the `previousViewControllers` parameter is the same as what the [viewControllers](../uipageviewcontroller/viewcontrollers.md) method would have returned prior to the page turn.

## See Also

### Responding to Page View Controller Events

- [- pageViewController:willTransitionToViewControllers:](<pageviewcontroller(__willtransitionto_).md>) — Called before a gesture-driven transition begins.
- [- pageViewController:spineLocationForInterfaceOrientation:](<pageviewcontroller(__spinelocationfor_).md>) — Returns the spine location for the given orientation.
