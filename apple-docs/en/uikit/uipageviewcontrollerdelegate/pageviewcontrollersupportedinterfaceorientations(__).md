---
title: 'pageViewControllerSupportedInterfaceOrientations(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollersupportedinterfaceorientations(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollersupportedinterfaceorientations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollersupportedinterfaceorientations%28_%3A%29.json'
content_hash: 'sha256:5d0b1733c6fece74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewControllerDelegate](../uipageviewcontrollerdelegate.md)

# pageViewControllerSupportedInterfaceOrientations(_:)

<sub>Instance Method</sub>

Returns the complete set of supported interface orientations for the page view controller, as determined by the delegate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pageViewControllerSupportedInterfaceOrientations(_ pageViewController: UIPageViewController) -> UIInterfaceOrientationMask
```

## Parameters

- `pageViewController` — The page view controller.

## Return Value

One of the [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md) constants that represents the set of   interface orientations supported by the page view controller.

## See Also

### Related Documentation

- [supportedInterfaceOrientations](../uiviewcontroller/supportedinterfaceorientations.md) — The interface orientations that the view controller supports.

### Overriding View Rotation Settings

- [- pageViewControllerPreferredInterfaceOrientationForPresentation:](<pageviewcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Returns the preferred orientation for presentation of the page view controller, as determined by the delegate.
