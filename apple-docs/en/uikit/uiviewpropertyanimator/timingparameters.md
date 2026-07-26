---
title: timingParameters
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/timingparameters
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/timingparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/timingparameters.json'
content_hash: 'sha256:8c1e21e46bbb4707'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# timingParameters

<sub>Instance Property</sub>

The information used to determine the timing curve for the animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var timingParameters: (any UITimingCurveProvider)? { get }
```

## Discussion

The timing curve defines the speed of the animation at different points during its execution. For a linear animation, the speed of the animation is constant over the total duration. For animations that follow a curve, the animation speeds up or slows down based on the slope of the curve. You specify the curve parameters at initialization time and can use this property to get those parameters later.

## See Also

### Accessing the animation parameters

- [duration](duration.md) — The total duration (in seconds) of the main animations.
- [delay](delay.md) — The delay (in seconds) after which the animations begin.
- [interruptible](isinterruptible.md) — A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value indicating whether views receive touch events while animations are running.
- [manualHitTestingEnabled](ismanualhittestingenabled.md) — A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [scrubsLinearly](scrubslinearly.md) — A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [pausesOnCompletion](pausesoncompletion.md) — A Boolean value that indicates whether a completed animation remains in the active state.
