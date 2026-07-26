---
title: prefersInterfaceOrientationLocked
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/prefersinterfaceorientationlocked
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/prefersinterfaceorientationlocked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/prefersinterfaceorientationlocked.json'
content_hash: 'sha256:022305253720f7f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# prefersInterfaceOrientationLocked

<sub>Instance Property</sub>

A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var prefersInterfaceOrientationLocked: Bool { get }
```

## Discussion

The default is [false](../../swift/false.md). Set this property to [true](../../swift/true.md) to indicate the view controller’s preference to lock the scene’s interface orientation. Check `UIWindowScene.effectiveGeometry.isInterfaceOrientationLocked` for the current state of the interface orientation lock. The system will consider locking the interface orientation when these conditions are true:

- The scene is centered on the screen
- The scene is the same size as the screen
- The scene is not occluded by another scene

The system continuously monitors the state and when the app no longer satisfies the requirements, it disables the interface orientation lock.

If you change the value of `prefersInterfaceOrientationLocked`, call [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<setneedsupdateofprefersinterfaceorientationlocked().md>).

## See Also

### Configuring the view rotation settings

- [supportedInterfaceOrientations](supportedinterfaceorientations.md) — The interface orientations that the view controller supports.
- [preferredInterfaceOrientationForPresentation](preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.
- [- setNeedsUpdateOfSupportedInterfaceOrientations](<setneedsupdateofsupportedinterfaceorientations().md>) — Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<setneedsupdateofprefersinterfaceorientationlocked().md>) — Indicates that the view controller changed the interface orientation lock preference.
- [childViewControllerForInterfaceOrientationLock](childforinterfaceorientationlock.md) — A child view controller to query for the interface orientation lock preference.
