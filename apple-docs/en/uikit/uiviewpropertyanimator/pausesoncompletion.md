---
title: pausesOnCompletion
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/pausesoncompletion
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/pausesoncompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/pausesoncompletion.json'
content_hash: 'sha256:ade1a6e13982b891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# pausesOnCompletion

<sub>Instance Property</sub>

A Boolean value that indicates whether a completed animation remains in the active state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var pausesOnCompletion: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the animator remains in the [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md) state when the animation finishes, and it does not execute its completion handler. Keeping the animator in the [UIViewAnimatingStateActive](../uiviewanimatingstate/active.md) state allows you to reverse the animation even after it has finished. When the value of this property is [false](../../swift/false.md), the animator automatically transitions to the [UIViewAnimatingStateInactive](../uiviewanimatingstate/inactive.md) state when the animation finishes, thereby concluding the animation. The default value of this property is [false](../../swift/false.md).

Because the completion handler is not called when this property is [true](../../swift/true.md), you cannot use the animator’s completion handler to determine when the animations have finished running. Instead, you determine when the animation has ended by observing the [running](../uiviewanimating/isrunning.md) property.

## See Also

### Accessing the animation parameters

- [duration](duration.md) — The total duration (in seconds) of the main animations.
- [delay](delay.md) — The delay (in seconds) after which the animations begin.
- [timingParameters](timingparameters.md) — The information used to determine the timing curve for the animation.
- [interruptible](isinterruptible.md) — A Boolean value indicating whether the animator is interruptible and can be paused or stopped.
- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value indicating whether views receive touch events while animations are running.
- [manualHitTestingEnabled](ismanualhittestingenabled.md) — A Boolean value indicating whether your app manages hit-testing while animations are in progress.
- [scrubsLinearly](scrubslinearly.md) — A Boolean value indicating whether a paused animation scrubs linearly or uses its specified timing information.
