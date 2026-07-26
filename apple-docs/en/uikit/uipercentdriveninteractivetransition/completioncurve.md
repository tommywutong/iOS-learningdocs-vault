---
title: completionCurve
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/completioncurve
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/completioncurve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/completioncurve.json'
content_hash: 'sha256:d19eae914eac566c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# completionCurve

<sub>Instance Property</sub>

Indicates the animation completion curve for an interactive transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var completionCurve: UIView.AnimationCurve { get set }
```

## Discussion

When the interactive part of a view controller transition is complete, you can set this property to indicate a desired animation completion curve. Default value is [UIViewAnimationCurveEaseInOut](../uiview/animationcurve/easeinout.md).

During the interactive portion of a view controller transition, the animation curve is linear.

## See Also

### Accessing transition attributes

- [timingCurve](timingcurve.md) — The timing curve to use when driving the animations.
- [duration](duration.md) — The overall duration (in seconds) of the transition animation.
- [percentComplete](percentcomplete.md) — The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [completionSpeed](completionspeed.md) — The speed of the transition animation.
- [wantsInteractiveStart](wantsinteractivestart.md) — A Boolean value indicating whether the animations are interactive initially.
