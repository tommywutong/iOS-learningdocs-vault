---
title: childViewControllerForPointerLock
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/childviewcontrollerforpointerlock
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerforpointerlock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childviewcontrollerforpointerlock.json'
content_hash: 'sha256:7c6dcc181eefcfb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childViewControllerForPointerLock

<sub>Instance Property</sub>

A child view controller to query for the pointer lock preference.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var childViewControllerForPointerLock: UIViewController? { get }
```

## Discussion

Call [- setNeedsUpdateOfPrefersPointerLocked](<setneedsupdateofpreferspointerlocked().md>) if the child view controller that the system needs to query for the pointer lock preference changes.

## See Also

### Managing pointer lock state

- [prefersPointerLocked](preferspointerlocked.md) — A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.
- [- setNeedsUpdateOfPrefersPointerLocked](<setneedsupdateofpreferspointerlocked().md>) — Indicates that the view controller changed the pointer lock preference.
