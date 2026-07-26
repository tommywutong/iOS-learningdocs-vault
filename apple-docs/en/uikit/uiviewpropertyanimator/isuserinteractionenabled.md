---
title: isUserInteractionEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/isuserinteractionenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/isuserinteractionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/isuserinteractionenabled.json'
content_hash: 'sha256:305f28f386107f3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# isUserInteractionEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether views receive touch events while animations are running.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isUserInteractionEnabled: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), touch events are delivered to views normally. Setting this property to [false](../../swift/false.md) causes touch events to be ignored in animated views for the duration of the animations. The default value of this property is [true](../../swift/true.md).

## See Also

### Accessing the animation parameters

- [duration](duration.md) — The total duration (in seconds) of the main animations.
- [delay](delay.md) — The delay (in seconds) after which the animations begin.
- [timingParameters](timingparameters.md) — The information used to determine the timing curve for the animation.
- [interruptible](isinterruptible.md) — A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [manualHitTestingEnabled](ismanualhittestingenabled.md) — A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [scrubsLinearly](scrubslinearly.md) — A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [pausesOnCompletion](pausesoncompletion.md) — A Boolean value that indicates whether a completed animation remains in the active state.
