---
title: delay
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/delay
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/delay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/delay.json'
content_hash: 'sha256:80d75b4dbb6ff9f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# delay

<sub>Instance Property</sub>

The delay (in seconds) after which the animations begin.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var delay: TimeInterval { get }
```

## Discussion

The default value of this property is `0`. When the value is greater than 0, the start of any animations is delayed by the specified amount of time.

To set a value for this property, use the [- startAnimationAfterDelay:](<../uiviewanimating/startanimation(afterdelay_).md>) method when starting your animations.

## See Also

### Accessing the animation parameters

- [duration](duration.md) — The total duration (in seconds) of the main animations.
- [timingParameters](timingparameters.md) — The information used to determine the timing curve for the animation.
- [interruptible](isinterruptible.md) — A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value indicating whether views receive touch events while animations are running.
- [manualHitTestingEnabled](ismanualhittestingenabled.md) — A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [scrubsLinearly](scrubslinearly.md) — A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [pausesOnCompletion](pausesoncompletion.md) — A Boolean value that indicates whether a completed animation remains in the active state.
