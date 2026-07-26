---
title: duration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition/duration
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition/duration.json'
content_hash: 'sha256:4c5e60c73810dbbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPercentDrivenInteractiveTransition](../uipercentdriveninteractivetransition.md)

# duration

<sub>Instance Property</sub>

The overall duration (in seconds) of the transition animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var duration: CGFloat { get }
```

## Discussion

This property reflects the duration of the transition animation if it were to occur without user interactions. It is obtained from the standard animator object returned by your delegate. The actual duration can vary depending on the user interactions you are tracking and responding to.

## See Also

### Related Documentation

- [- transitionDuration:](<../uiviewcontrolleranimatedtransitioning/transitionduration(using_).md>) — Asks your animator object for the duration (in seconds) of the transition animation.

### Accessing transition attributes

- [timingCurve](timingcurve.md) — The timing curve to use when driving the animations.
- [completionCurve](completioncurve.md) — Indicates the animation completion curve for an interactive transition.
- [percentComplete](percentcomplete.md) — The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [completionSpeed](completionspeed.md) — The speed of the transition animation.
- [wantsInteractiveStart](wantsinteractivestart.md) — A Boolean value indicating whether the animations are interactive initially.
