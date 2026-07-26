---
title: setNeedsUpdateOfSupportedInterfaceOrientations()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedsupdateofsupportedinterfaceorientations()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofsupportedinterfaceorientations()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedsupdateofsupportedinterfaceorientations%28%29.json'
content_hash: 'sha256:d8045d314d9b813d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsUpdateOfSupportedInterfaceOrientations()

<sub>Instance Method</sub>

Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsUpdateOfSupportedInterfaceOrientations()
```

## Discussion

By default, this method animates any changes to orientation. To perform a nonanimated update, call this method from [+ performWithoutAnimation:](<../uiview/performwithoutanimation(__).md>).

## See Also

### Configuring the view rotation settings

- [supportedInterfaceOrientations](supportedinterfaceorientations.md) — The interface orientations that the view controller supports.
- [preferredInterfaceOrientationForPresentation](preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.
- [prefersInterfaceOrientationLocked](prefersinterfaceorientationlocked.md) — A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<setneedsupdateofprefersinterfaceorientationlocked().md>) — Indicates that the view controller changed the interface orientation lock preference.
- [childViewControllerForInterfaceOrientationLock](childforinterfaceorientationlock.md) — A child view controller to query for the interface orientation lock preference.
