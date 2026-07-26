---
title: percentComplete
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/percentcomplete
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/percentcomplete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/percentcomplete.json'
content_hash: 'sha256:377d74fff9ae01a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# percentComplete

<sub>Instance Property</sub>

The amount of the transition (specified as a percentage of the overall duration) that’s complete.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var percentComplete: CGFloat { get }
```

## Discussion

The value in this property reflects the last value passed to the [- updateInteractiveTransition:](<update(__).md>) method.

## See Also

### Related Documentation

- [- updateInteractiveTransition:](<update(__).md>) — Updates the completion percentage of the transition.

### Accessing transition attributes

- [timingCurve](timingcurve.md) — The timing curve to use when driving the animations.
- [completionCurve](completioncurve.md) — Indicates the animation completion curve for an interactive transition.
- [duration](duration.md) — The overall duration (in seconds) of the transition animation.
- [completionSpeed](completionspeed.md) — The speed of the transition animation.
- [wantsInteractiveStart](wantsinteractivestart.md) — A Boolean value indicating whether the animations are interactive initially.
