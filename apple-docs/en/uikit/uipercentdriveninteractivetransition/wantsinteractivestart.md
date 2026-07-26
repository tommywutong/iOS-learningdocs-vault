---
title: wantsInteractiveStart
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/wantsinteractivestart
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/wantsinteractivestart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/wantsinteractivestart.json'
content_hash: 'sha256:b5fc6cdf5b98f045'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# wantsInteractiveStart

<sub>Instance Property</sub>

A Boolean value indicating whether the animations are interactive initially.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var wantsInteractiveStart: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), interactive animations start as paused, allowing you to drive the animations yourself from the start. You might set this property to [false](../../swift/false.md) when you want to start your animations without interactivity. The default value of this property is [true](../../swift/true.md).

## See Also

### Accessing transition attributes

- [timingCurve](timingcurve.md) — The timing curve to use when driving the animations.
- [completionCurve](completioncurve.md) — Indicates the animation completion curve for an interactive transition.
- [duration](duration.md) — The overall duration (in seconds) of the transition animation.
- [percentComplete](percentcomplete.md) — The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [completionSpeed](completionspeed.md) — The speed of the transition animation.
