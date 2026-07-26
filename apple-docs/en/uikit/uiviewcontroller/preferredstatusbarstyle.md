---
title: preferredStatusBarStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/preferredstatusbarstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferredstatusbarstyle.json'
content_hash: 'sha256:d61a782345c828a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# preferredStatusBarStyle

<sub>Instance Property</sub>

The preferred status bar style for the view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredStatusBarStyle: UIStatusBarStyle { get }
```

## Return Value

A [UIStatusBarStyle](../uistatusbarstyle.md) key indicating your preferred status bar style for the view controller.

## Discussion

You can override the preferred status bar style for a view controller by implementing the [childViewControllerForStatusBarStyle](childforstatusbarstyle.md) method.

If the return value from this method changes, call the [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) method.

## See Also

### Managing the status bar

- [prefersStatusBarHidden](prefersstatusbarhidden.md) — Specifies whether the view controller prefers the status bar to be hidden or shown.
- [childViewControllerForStatusBarHidden](childforstatusbarhidden.md) — The view controller to use for determining the hidden state of the status bar.
- [childViewControllerForStatusBarStyle](childforstatusbarstyle.md) — Called when the system needs the view controller to use for determining status bar style.
- [UIStatusBarStyle](../uistatusbarstyle.md) — Constants that describe the style of the device’s status bar.
- [modalPresentationCapturesStatusBarAppearance](modalpresentationcapturesstatusbarappearance.md) — Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [preferredStatusBarUpdateAnimation](preferredstatusbarupdateanimation.md) — Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) — Indicates to the system that the view controller status bar attributes have changed.
