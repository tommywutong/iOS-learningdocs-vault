---
title: 'setViewControllers(_:direction:animated:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/setviewcontrollers(_:direction:animated:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/setviewcontrollers%28_%3Adirection%3Aanimated%3Acompletion%3A%29.json'
content_hash: 'sha256:8335c8b5fcfac115'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# setViewControllers(_:direction:animated:completion:)

<sub>Instance Method</sub>

Sets the view controllers to be displayed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setViewControllers(_ viewControllers: [UIViewController]?, direction: UIPageViewController.NavigationDirection, animated: Bool, completion: ((Bool) -> Void)? = nil)
```

## Parameters

- `viewControllers` — The view controller or view controllers to be displayed.

- `direction` — The navigation direction.

- `animated` — A Boolean value that indicates whether the transition is to be animated.

- `completion` — A block to be called when the page-turn animation completes. The block takes the following parameters: - **_finished_** — [true](../../swift/true.md) if the animation finished; [false](../../swift/false.md) if it was skipped.

## Discussion

The view controllers passed to this method are those that will be visible after the animation has completed. Use a data source to provide additional view controllers to which users navigate.

If the transition style is [UIPageViewControllerTransitionStylePageCurl](transitionstyle-swift.enum/pagecurl.md), the view controllers to pass in the `viewControllers` parameter depends on the spine location and the value of the [doubleSided](isdoublesided.md) property:

| Spine location | Double sided | What to pass |
|---|---|---|
| [UIPageViewControllerSpineLocationMid](spinelocation-swift.enum/mid.md) | [true](../../swift/true.md) | Pass the page to be displayed on the left and the page to be displayed on the right. |
| [UIPageViewControllerSpineLocationMin](spinelocation-swift.enum/min.md) or [UIPageViewControllerSpineLocationMax](spinelocation-swift.enum/max.md) | [true](../../swift/true.md) | Pass the front of the page to be displayed and the back of the previously-displayed page. The back is used for the page turning animation. |
| [UIPageViewControllerSpineLocationMin](spinelocation-swift.enum/min.md) or [UIPageViewControllerSpineLocationMax](spinelocation-swift.enum/max.md) | [false](../../swift/false.md) | Pass the front of the page to be displayed. |

## See Also

### Providing Content

- [NavigationDirection](navigationdirection.md) — Directions for page-turn transitions.
- [viewControllers](viewcontrollers.md) — The view controllers displayed by the page view controller.
- [gestureRecognizers](gesturerecognizers.md) — An array of [UIGestureRecognizer](../uigesturerecognizer.md) objects that are configured to handle user interaction.
