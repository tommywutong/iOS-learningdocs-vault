---
title: 'splitViewController(_:willChangeTo:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willchangeto:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willchangeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Awillchangeto%3A%29.json'
content_hash: 'sha256:01d086c473fd2052'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:willChangeTo:)

<sub>Instance Method</sub>

Tells the delegate that the display mode for the split view controller is about to change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ svc: UISplitViewController, willChangeTo displayMode: UISplitViewController.DisplayMode)
```

## Parameters

- `svc` — The split view controller whose display mode is changing.

- `displayMode` — The new display mode that is about to be applied to the split view controller.

## Discussion

The split view controller calls this method when its display mode is about to change. Because changing the display mode usually means hiding or showing one of the child view controllers, you can implement this method and use it to add or remove the controls for showing the primary view controller.

## See Also

### Responding to display mode changes

- [- targetDisplayModeForActionInSplitViewController:](<targetdisplaymodeforaction(in_).md>) — Asks the delegate to provide the display mode to apply when a split view controller action occurs.
