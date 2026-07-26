---
title: 'splitViewControllerSupportedInterfaceOrientations(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollersupportedinterfaceorientations(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollersupportedinterfaceorientations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollersupportedinterfaceorientations%28_%3A%29.json'
content_hash: 'sha256:2503c683cd3fc523'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewControllerSupportedInterfaceOrientations(_:)

<sub>Instance Method</sub>

Asks the delegate to specify the interface orientations that the split view controller supports.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func splitViewControllerSupportedInterfaceOrientations(_ splitViewController: UISplitViewController) -> UIInterfaceOrientationMask
```

## Parameters

- `splitViewController` — The split view controller.

## Return Value

The orientations that you want the specified split view controller to support. The value you return can be one or more of the [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md) constants.

## Discussion

The split view controller calls this method to obtain the orientations that it supports. You can use this method to alter the set of orientations typically supported by a split view controller. If you don’t implement this method, the split view controller supports all orientations on iPad and all but the [UIInterfaceOrientationMaskAllButUpsideDown](../uiinterfaceorientationmask/allbutupsidedown.md) orientation on iPhone devices.

## See Also

### Related Documentation

- [supportedInterfaceOrientations](../uiviewcontroller/supportedinterfaceorientations.md) — The interface orientations that the view controller supports.

### Specifying the interface orientations

- [- splitViewControllerPreferredInterfaceOrientationForPresentation:](<splitviewcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Asks the delegate for the orientation to use when presenting the split view controller.
