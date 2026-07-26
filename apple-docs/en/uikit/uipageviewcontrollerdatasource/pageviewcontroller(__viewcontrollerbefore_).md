---
title: 'pageViewController(_:viewControllerBefore:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontrollerdatasource/pageviewcontroller(_:viewcontrollerbefore:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/pageviewcontroller(_:viewcontrollerbefore:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdatasource/pageviewcontroller%28_%3Aviewcontrollerbefore%3A%29.json'
content_hash: 'sha256:06d166ce695deaab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewControllerDataSource](../uipageviewcontrollerdatasource.md)

# pageViewController(_:viewControllerBefore:)

<sub>Instance Method</sub>

Returns the view controller before the given view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pageViewController(_ pageViewController: UIPageViewController, viewControllerBefore viewController: UIViewController) -> UIViewController?
```

## Parameters

- `pageViewController` — The page view controller

- `viewController` — The view controller that the user navigated away from.

## Return Value

The view controller before the given view controller, or `nil` to indicate that there is no previous view controller.

## See Also

### Providing View Controllers

- [- pageViewController:viewControllerAfterViewController:](<pageviewcontroller(__viewcontrollerafter_).md>) — Returns the view controller after the given view controller.
