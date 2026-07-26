---
title: completionSpeed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/completionspeed
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/completionspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/completionspeed.json'
content_hash: 'sha256:42a25f2c050c1a68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# completionSpeed

<sub>Instance Property</sub>

The speed of the transition animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var completionSpeed: CGFloat { get set }
```

## Discussion

The default value of this property is `1.0`, which yields an animation that proceeds in real time. You typically change this value to speed up or slow down the animation at specific points in the transition. For example, you might change the animation speed at the end of a transition or when canceling it, in which case you would set the speed when you stop tracking user events and are about to call the [- cancelInteractiveTransition](<cancel().md>) or [- finishInteractiveTransition](<finish().md>) method.

The speed acts as a multiplier to the current animation speed, so values greater than `1.0` speed up the animation and values less than `1.0` slow it down. The value in this property must always be greater than `0.0`.

## See Also

### Accessing transition attributes

- [timingCurve](timingcurve.md) — The timing curve to use when driving the animations.
- [completionCurve](completioncurve.md) — Indicates the animation completion curve for an interactive transition.
- [duration](duration.md) — The overall duration (in seconds) of the transition animation.
- [percentComplete](percentcomplete.md) — The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [wantsInteractiveStart](wantsinteractivestart.md) — A Boolean value indicating whether the animations are interactive initially.
