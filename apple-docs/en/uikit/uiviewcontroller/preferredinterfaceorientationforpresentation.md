---
title: preferredInterfaceOrientationForPresentation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/preferredinterfaceorientationforpresentation
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredinterfaceorientationforpresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferredinterfaceorientationforpresentation.json'
content_hash: 'sha256:a2c1502157b420f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# preferredInterfaceOrientationForPresentation

<sub>Instance Property</sub>

The interface orientation to use when presenting the view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }
```

## Return Value

The interface orientation with which to present the view controller.

## Discussion

The system calls this method when presenting the view controller full screen. When your view controller supports two or more orientations but the content appears best in one of those orientations, override this method and return the preferred orientation.

If your view controller implements this method, your view controller’s view is shown in the preferred orientation (although it can later be rotated to another supported rotation). If you do not implement this method, the system presents the view controller using the current orientation of the status bar.

## See Also

### Configuring the view rotation settings

- [supportedInterfaceOrientations](supportedinterfaceorientations.md) — The interface orientations that the view controller supports.
- [- setNeedsUpdateOfSupportedInterfaceOrientations](<setneedsupdateofsupportedinterfaceorientations().md>) — Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [prefersInterfaceOrientationLocked](prefersinterfaceorientationlocked.md) — A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<setneedsupdateofprefersinterfaceorientationlocked().md>) — Indicates that the view controller changed the interface orientation lock preference.
- [childViewControllerForInterfaceOrientationLock](childforinterfaceorientationlock.md) — A child view controller to query for the interface orientation lock preference.
