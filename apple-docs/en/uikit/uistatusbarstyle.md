---
title: UIStatusBarStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistatusbarstyle
source_url: 'https://developer.apple.com/documentation/uikit/uistatusbarstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistatusbarstyle.json'
content_hash: 'sha256:954c2c2fca6618c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStatusBarStyle

<sub>Enumeration</sub>

Constants that describe the style of the device’s status bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIStatusBarStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIStatusBarStyleDefault](uistatusbarstyle/default.md) — A style that automatically selects an appearance for the status bar and updates it dynamically to maintain contrast with the content below it.
- [UIStatusBarStyleLightContent](uistatusbarstyle/lightcontent.md) — A light status bar, intended for use on dark backgrounds.
- [UIStatusBarStyleDarkContent](uistatusbarstyle/darkcontent.md) — A dark status bar, intended for use on light backgrounds.

### Initializers

- [init(rawValue:)](<uistatusbarstyle/init(rawvalue_).md>)

## See Also

### Managing the status bar

- [prefersStatusBarHidden](uiviewcontroller/prefersstatusbarhidden.md) — Specifies whether the view controller prefers the status bar to be hidden or shown.
- [childViewControllerForStatusBarHidden](uiviewcontroller/childforstatusbarhidden.md) — The view controller to use for determining the hidden state of the status bar.
- [childViewControllerForStatusBarStyle](uiviewcontroller/childforstatusbarstyle.md) — Called when the system needs the view controller to use for determining status bar style.
- [preferredStatusBarStyle](uiviewcontroller/preferredstatusbarstyle.md) — The preferred status bar style for the view controller.
- [modalPresentationCapturesStatusBarAppearance](uiviewcontroller/modalpresentationcapturesstatusbarappearance.md) — Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [preferredStatusBarUpdateAnimation](uiviewcontroller/preferredstatusbarupdateanimation.md) — Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [- setNeedsStatusBarAppearanceUpdate](<uiviewcontroller/setneedsstatusbarappearanceupdate().md>) — Indicates to the system that the view controller status bar attributes have changed.
