---
title: duration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/duration
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/duration.json'
content_hash: 'sha256:cfe68bd0d68dee9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# duration

<sub>Instance Property</sub>

The total duration (in seconds) of the main animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var duration: TimeInterval { get }
```

## Discussion

You set the duration value when creating the animator and cannot change it later. Animations added while the animator is in the inactive state are run for the specified duration. Animations added later run only for the remaining time, which is determined by the formula `(1.0 - fractionComplete) * duration`.

## See Also

### Accessing the animation parameters

- [delay](delay.md) — The delay (in seconds) after which the animations begin.
- [timingParameters](timingparameters.md) — The information used to determine the timing curve for the animation.
- [interruptible](isinterruptible.md) — A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value indicating whether views receive touch events while animations are running.
- [manualHitTestingEnabled](ismanualhittestingenabled.md) — A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [scrubsLinearly](scrubslinearly.md) — A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [pausesOnCompletion](pausesoncompletion.md) — A Boolean value that indicates whether a completed animation remains in the active state.
