---
title: setNeedsStatusBarAppearanceUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedsstatusbarappearanceupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsstatusbarappearanceupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedsstatusbarappearanceupdate%28%29.json'
content_hash: 'sha256:11bd374a89292ae2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsStatusBarAppearanceUpdate()

<sub>Instance Method</sub>

Indicates to the system that the view controller status bar attributes have changed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setNeedsStatusBarAppearanceUpdate()
```

## Discussion

Call this method if the view controller’s status bar attributes, such as hidden/unhidden status or style, change. If you call this method within an animation block, the changes are animated along with the rest of the animation block.

## See Also

### Managing the status bar

- [prefersStatusBarHidden](prefersstatusbarhidden.md) — Specifies whether the view controller prefers the status bar to be hidden or shown.
- [childViewControllerForStatusBarHidden](childforstatusbarhidden.md) — The view controller to use for determining the hidden state of the status bar.
- [childViewControllerForStatusBarStyle](childforstatusbarstyle.md) — Called when the system needs the view controller to use for determining status bar style.
- [preferredStatusBarStyle](preferredstatusbarstyle.md) — The preferred status bar style for the view controller.
- [UIStatusBarStyle](../uistatusbarstyle.md) — Constants that describe the style of the device’s status bar.
- [modalPresentationCapturesStatusBarAppearance](modalpresentationcapturesstatusbarappearance.md) — Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [preferredStatusBarUpdateAnimation](preferredstatusbarupdateanimation.md) — Specifies the animation style to use for hiding and showing the status bar for the view controller.
