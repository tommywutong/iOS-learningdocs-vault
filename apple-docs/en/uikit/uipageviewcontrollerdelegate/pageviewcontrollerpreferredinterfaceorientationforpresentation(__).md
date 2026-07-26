---
title: 'pageViewControllerPreferredInterfaceOrientationForPresentation(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation%28_%3A%29.json'
content_hash: 'sha256:dd56f5b90acc6eea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewControllerDelegate](../uipageviewcontrollerdelegate.md)

# pageViewControllerPreferredInterfaceOrientationForPresentation(_:)

<sub>Instance Method</sub>

Returns the preferred orientation for presentation of the page view controller, as determined by the delegate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pageViewControllerPreferredInterfaceOrientationForPresentation(_ pageViewController: UIPageViewController) -> UIInterfaceOrientation
```

## Parameters

- `pageViewController` — The page view controller.

## Return Value

The preferred orientation for presenting the page view controller.

## See Also

### Related Documentation

- [preferredInterfaceOrientationForPresentation](../uiviewcontroller/preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.

### Overriding View Rotation Settings

- [- pageViewControllerSupportedInterfaceOrientations:](<pageviewcontrollersupportedinterfaceorientations(__).md>) — Returns the complete set of supported interface orientations for the page view controller, as determined by the delegate.
