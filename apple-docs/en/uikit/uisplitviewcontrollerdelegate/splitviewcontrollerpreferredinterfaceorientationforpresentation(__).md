---
title: 'splitViewControllerPreferredInterfaceOrientationForPresentation(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerpreferredinterfaceorientationforpresentation(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerpreferredinterfaceorientationforpresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerpreferredinterfaceorientationforpresentation%28_%3A%29.json'
content_hash: 'sha256:30b3b50574c89000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewControllerPreferredInterfaceOrientationForPresentation(_:)

<sub>Instance Method</sub>

Asks the delegate for the orientation to use when presenting the split view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func splitViewControllerPreferredInterfaceOrientationForPresentation(_ splitViewController: UISplitViewController) -> UIInterfaceOrientation
```

## Parameters

- `splitViewController` — The split view controller that is about to be presented onscreen.

## Return Value

The orientation to use when first displaying the split view controller.

## Discussion

UIKit calls this method to determine which orientation your app prefers when presenting the specified split view controller. You can use this method to specify the orientation that you think is best when first displaying the split view controller. The orientation you specify can be different from the current device orientation. After presentation, the system may rotate the split view controller as appropriate to one of its other supported interface orientations.

If you do not implement this method, the system presents the view controller using the current orientation of the status bar.

## See Also

### Related Documentation

- [preferredInterfaceOrientationForPresentation](../uiviewcontroller/preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.

### Specifying the interface orientations

- [- splitViewControllerSupportedInterfaceOrientations:](<splitviewcontrollersupportedinterfaceorientations(__).md>) — Asks the delegate to specify the interface orientations that the split view controller supports.
