---
title: prefersStatusBarHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/prefersstatusbarhidden
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/prefersstatusbarhidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/prefersstatusbarhidden.json'
content_hash: 'sha256:fc64a0504194b326'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# prefersStatusBarHidden

<sub>Instance Property</sub>

Specifies whether the view controller prefers the status bar to be hidden or shown.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var prefersStatusBarHidden: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the status bar should be hidden or [false](../../swift/false.md) if it should be shown.

## Discussion

If you change the return value for this method, call the [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) method. To specify that a child view controller should control preferred status bar hidden/unhidden state, implement the [childViewControllerForStatusBarHidden](childforstatusbarhidden.md) method.

By default, this method returns [false](../../swift/false.md) with one exception. For apps linked against iOS 8 or later, this method returns [true](../../swift/true.md) if the view controller is in a vertically compact environment.

## See Also

### Managing the status bar

- [childViewControllerForStatusBarHidden](childforstatusbarhidden.md) — The view controller to use for determining the hidden state of the status bar.
- [childViewControllerForStatusBarStyle](childforstatusbarstyle.md) — Called when the system needs the view controller to use for determining status bar style.
- [preferredStatusBarStyle](preferredstatusbarstyle.md) — The preferred status bar style for the view controller.
- [UIStatusBarStyle](../uistatusbarstyle.md) — Constants that describe the style of the device’s status bar.
- [modalPresentationCapturesStatusBarAppearance](modalpresentationcapturesstatusbarappearance.md) — Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [preferredStatusBarUpdateAnimation](preferredstatusbarupdateanimation.md) — Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) — Indicates to the system that the view controller status bar attributes have changed.
