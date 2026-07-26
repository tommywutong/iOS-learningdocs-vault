---
title: preferredStatusBarUpdateAnimation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/preferredstatusbarupdateanimation
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarupdateanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferredstatusbarupdateanimation.json'
content_hash: 'sha256:e38d61af5dac6af2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# preferredStatusBarUpdateAnimation

<sub>Instance Property</sub>

Specifies the animation style to use for hiding and showing the status bar for the view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredStatusBarUpdateAnimation: UIStatusBarAnimation { get }
```

## Return Value

The style of status bar animation to use; one of the constants from the [UIStatusBarAnimation](../uistatusbaranimation.md) enum. Default value is [UIStatusBarAnimationFade](../uistatusbaranimation/fade.md).

## Discussion

This property comes into play only when you actively change the status bar’s show/hide state by changing the return value of the [prefersStatusBarHidden](prefersstatusbarhidden.md) method.

## See Also

### Managing the status bar

- [prefersStatusBarHidden](prefersstatusbarhidden.md) — Specifies whether the view controller prefers the status bar to be hidden or shown.
- [childViewControllerForStatusBarHidden](childforstatusbarhidden.md) — The view controller to use for determining the hidden state of the status bar.
- [childViewControllerForStatusBarStyle](childforstatusbarstyle.md) — Called when the system needs the view controller to use for determining status bar style.
- [preferredStatusBarStyle](preferredstatusbarstyle.md) — The preferred status bar style for the view controller.
- [UIStatusBarStyle](../uistatusbarstyle.md) — Constants that describe the style of the device’s status bar.
- [modalPresentationCapturesStatusBarAppearance](modalpresentationcapturesstatusbarappearance.md) — Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) — Indicates to the system that the view controller status bar attributes have changed.
