---
title: 'pageViewController(_:spineLocationFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller(_:spinelocationfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontroller%28_%3Aspinelocationfor%3A%29.json'
content_hash: 'sha256:ea87b33c709c928d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewControllerDelegate](../uipageviewcontrollerdelegate.md)

# pageViewController(_:spineLocationFor:)

<sub>Instance Method</sub>

Returns the spine location for the given orientation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pageViewController(_ pageViewController: UIPageViewController, spineLocationFor orientation: UIInterfaceOrientation) -> UIPageViewController.SpineLocation
```

## Parameters

- `pageViewController` — The page view controller

- `orientation` — The new orientation.

## Return Value

The spine location.

## Discussion

Use this method to change the spine location when the device orientation changes, as well as setting new view controllers and changing the double-sided state.

This method is called only if the transition style is [UIPageViewControllerTransitionStylePageCurl](../uipageviewcontroller/transitionstyle-swift.enum/pagecurl.md).

## See Also

### Responding to Page View Controller Events

- [- pageViewController:willTransitionToViewControllers:](<pageviewcontroller(__willtransitionto_).md>) — Called before a gesture-driven transition begins.
- [- pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:](<pageviewcontroller(__didfinishanimating_previousviewcontrollers_transitioncompleted_).md>) — Called after a gesture-driven transition completes.
