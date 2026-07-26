---
title: completionCurve
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollerinteractivetransitioning/completioncurve
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/completioncurve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerinteractivetransitioning/completioncurve.json'
content_hash: 'sha256:eb6e3c637a1806b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md)

# completionCurve

<sub>Instance Property</sub>

Called when the system needs the animation completion curve for an interactive view controller transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var completionCurve: UIView.AnimationCurve { get }
```

## Return Value

Default value is [UIViewAnimationCurveEaseInOut](../uiview/animationcurve/easeinout.md), with other possible values described in the [AnimationCurve](../uiview/animationcurve.md) type definition.

## See Also

### Providing a transition’s completion characteristics

- [completionSpeed](completionspeed.md) — Called when the system needs the speed at which to complete an interactive transition, after the interactive portion is finished.
