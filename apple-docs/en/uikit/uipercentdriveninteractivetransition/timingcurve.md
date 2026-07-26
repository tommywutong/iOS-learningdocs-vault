---
title: timingCurve
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/timingcurve
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/timingcurve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/timingcurve.json'
content_hash: 'sha256:d56353259ff93904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# timingCurve

<sub>Instance Property</sub>

The timing curve to use when driving the animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var timingCurve: (any UITimingCurveProvider)? { get set }
```

## See Also

### Accessing transition attributes

- [completionCurve](completioncurve.md) — Indicates the animation completion curve for an interactive transition.
- [duration](duration.md) — The overall duration (in seconds) of the transition animation.
- [percentComplete](percentcomplete.md) — The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [completionSpeed](completionspeed.md) — The speed of the transition animation.
- [wantsInteractiveStart](wantsinteractivestart.md) — A Boolean value indicating whether the animations are interactive initially.
