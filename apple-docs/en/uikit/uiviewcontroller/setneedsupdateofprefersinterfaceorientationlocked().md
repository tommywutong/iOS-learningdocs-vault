---
title: setNeedsUpdateOfPrefersInterfaceOrientationLocked()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked%28%29.json'
content_hash: 'sha256:208ec6ea3f8872fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsUpdateOfPrefersInterfaceOrientationLocked()

<sub>Instance Method</sub>

Indicates that the view controller changed the interface orientation lock preference.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setNeedsUpdateOfPrefersInterfaceOrientationLocked()
```

## See Also

### Configuring the view rotation settings

- [supportedInterfaceOrientations](supportedinterfaceorientations.md) — The interface orientations that the view controller supports.
- [preferredInterfaceOrientationForPresentation](preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.
- [- setNeedsUpdateOfSupportedInterfaceOrientations](<setneedsupdateofsupportedinterfaceorientations().md>) — Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [prefersInterfaceOrientationLocked](prefersinterfaceorientationlocked.md) — A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [childViewControllerForInterfaceOrientationLock](childforinterfaceorientationlock.md) — A child view controller to query for the interface orientation lock preference.
