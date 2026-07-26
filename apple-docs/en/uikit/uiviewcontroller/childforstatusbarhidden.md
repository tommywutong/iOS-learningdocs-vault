---
title: childForStatusBarHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/childforstatusbarhidden
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childforstatusbarhidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childforstatusbarhidden.json'
content_hash: 'sha256:8a301f111495ebbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childForStatusBarHidden

<sub>Instance Property</sub>

The view controller to use for determining the hidden state of the status bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var childForStatusBarHidden: UIViewController? { get }
```

## Discussion

If your container view controller derives the hidden state of the status bar from one of its child view controllers, implement this property to specify which child view controller you want to control the hidden/unhidden state. If you return `nil` or don’t override this property, the status bar hidden/unhidden state for `self` is used.

Call [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) if the child view controller for determining the hidden state of the status bar changes.

## See Also

### Managing the status bar

- [prefersStatusBarHidden](prefersstatusbarhidden.md) — Specifies whether the view controller prefers the status bar to be hidden or shown.
- [childViewControllerForStatusBarStyle](childforstatusbarstyle.md) — Called when the system needs the view controller to use for determining status bar style.
- [preferredStatusBarStyle](preferredstatusbarstyle.md) — The preferred status bar style for the view controller.
- [UIStatusBarStyle](../uistatusbarstyle.md) — Constants that describe the style of the device’s status bar.
- [modalPresentationCapturesStatusBarAppearance](modalpresentationcapturesstatusbarappearance.md) — Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [preferredStatusBarUpdateAnimation](preferredstatusbarupdateanimation.md) — Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) — Indicates to the system that the view controller status bar attributes have changed.
