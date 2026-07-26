---
title: isManualHitTestingEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/ismanualhittestingenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/ismanualhittestingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/ismanualhittestingenabled.json'
content_hash: 'sha256:27753d6fa33f9bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# isManualHitTestingEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether your app manages hit-testing while animations are in progress.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isManualHitTestingEnabled: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md).

## See Also

### Accessing the animation parameters

- [duration](duration.md) — The total duration (in seconds) of the main animations.
- [delay](delay.md) — The delay (in seconds) after which the animations begin.
- [timingParameters](timingparameters.md) — The information used to determine the timing curve for the animation.
- [interruptible](isinterruptible.md) — A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value indicating whether views receive touch events while animations are running.
- [scrubsLinearly](scrubslinearly.md) — A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [pausesOnCompletion](pausesoncompletion.md) — A Boolean value that indicates whether a completed animation remains in the active state.
