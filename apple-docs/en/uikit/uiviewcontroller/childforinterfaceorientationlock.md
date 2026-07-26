---
title: childForInterfaceOrientationLock
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/childforinterfaceorientationlock
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childforinterfaceorientationlock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childforinterfaceorientationlock.json'
content_hash: 'sha256:80ba28720048b66c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childForInterfaceOrientationLock

<sub>Instance Property</sub>

A child view controller to query for the interface orientation lock preference.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var childForInterfaceOrientationLock: UIViewController? { get }
```

## Discussion

Override to return a child view controller or `nil`. If you return a view controller, the system uses that view controller’s preference for interface orientation lock. If you return `nil`, the system uses `self` to get the preference for interface orientation lock. Call [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<setneedsupdateofprefersinterfaceorientationlocked().md>) if the child view controller that the system needs to query for the interface orientation lock preference changes.

## See Also

### Configuring the view rotation settings

- [supportedInterfaceOrientations](supportedinterfaceorientations.md) — The interface orientations that the view controller supports.
- [preferredInterfaceOrientationForPresentation](preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.
- [- setNeedsUpdateOfSupportedInterfaceOrientations](<setneedsupdateofsupportedinterfaceorientations().md>) — Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [prefersInterfaceOrientationLocked](prefersinterfaceorientationlocked.md) — A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<setneedsupdateofprefersinterfaceorientationlocked().md>) — Indicates that the view controller changed the interface orientation lock preference.
