---
title: isInterruptible
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/isinterruptible
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/isinterruptible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/isinterruptible.json'
content_hash: 'sha256:1207858a87b9cccd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# isInterruptible

<sub>Instance Property</sub>

A Boolean value indicating whether the animator is interruptible and can be paused or stopped.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isInterruptible: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), you can use the [- pauseAnimation](<../uiviewanimating/pauseanimation().md>) and [- stopAnimation:](<../uiviewanimating/stopanimation(__).md>) methods to interrupt the animations and make changes. When the value of this property is [false](../../swift/false.md), the animations run to completion (and without interruption) after you call the [- startAnimation](<../uiviewanimating/startanimation().md>) method. If you use a view property animator object to implement an interruptible view controller transition, this property must be [true](../../swift/true.md).

It is a programmer error to change this property if the animator’s [state](../uiviewanimating/state.md) property is not set to [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md).

## See Also

### Accessing the animation parameters

- [duration](duration.md) — The total duration (in seconds) of the main animations.
- [delay](delay.md) — The delay (in seconds) after which the animations begin.
- [timingParameters](timingparameters.md) — The information used to determine the timing curve for the animation.
- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value indicating whether views receive touch events while animations are running.
- [manualHitTestingEnabled](ismanualhittestingenabled.md) — A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [scrubsLinearly](scrubslinearly.md) — A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
- [pausesOnCompletion](pausesoncompletion.md) — A Boolean value that indicates whether a completed animation remains in the active state.
