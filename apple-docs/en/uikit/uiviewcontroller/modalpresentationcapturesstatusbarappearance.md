---
title: modalPresentationCapturesStatusBarAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/modalpresentationcapturesstatusbarappearance
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/modalpresentationcapturesstatusbarappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/modalpresentationcapturesstatusbarappearance.json'
content_hash: 'sha256:ba7d869ebb00b84b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# modalPresentationCapturesStatusBarAppearance

<sub>Instance Property</sub>

Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var modalPresentationCapturesStatusBarAppearance: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md).

When you present a view controller by calling the [- presentViewController:animated:completion:](<present(__animated_completion_).md>) method, status bar appearance control is transferred from the presenting to the presented view controller only if the presented controller’s [modalPresentationStyle](modalpresentationstyle.md) value is [UIModalPresentationFullScreen](../uimodalpresentationstyle/fullscreen.md). By setting this property to [true](../../swift/true.md), you specify the presented view controller controls status bar appearance, even though presented non-fullscreen.

The system ignores this property’s value for a view controller presented fullscreen.

## See Also

### Managing the status bar

- [prefersStatusBarHidden](prefersstatusbarhidden.md) — Specifies whether the view controller prefers the status bar to be hidden or shown.
- [childViewControllerForStatusBarHidden](childforstatusbarhidden.md) — The view controller to use for determining the hidden state of the status bar.
- [childViewControllerForStatusBarStyle](childforstatusbarstyle.md) — Called when the system needs the view controller to use for determining status bar style.
- [preferredStatusBarStyle](preferredstatusbarstyle.md) — The preferred status bar style for the view controller.
- [UIStatusBarStyle](../uistatusbarstyle.md) — Constants that describe the style of the device’s status bar.
- [preferredStatusBarUpdateAnimation](preferredstatusbarupdateanimation.md) — Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [- setNeedsStatusBarAppearanceUpdate](<setneedsstatusbarappearanceupdate().md>) — Indicates to the system that the view controller status bar attributes have changed.
