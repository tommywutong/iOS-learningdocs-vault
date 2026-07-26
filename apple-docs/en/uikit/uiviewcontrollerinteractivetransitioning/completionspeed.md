---
title: completionSpeed
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollerinteractivetransitioning/completionspeed
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/completionspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerinteractivetransitioning/completionspeed.json'
content_hash: 'sha256:3b4cd8bfeae23501'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md)

# completionSpeed

<sub>Instance Property</sub>

Called when the system needs the speed at which to complete an interactive transition, after the interactive portion is finished.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var completionSpeed: CGFloat { get }
```

## Return Value

Default value is `1.0`, which corresponds to the total (noninteractive) transition duration scaled by the percentage of the transition remaining. Value must be greater than `0.0`.

## See Also

### Providing a transition’s completion characteristics

- [completionCurve](completioncurve.md) — Called when the system needs the animation completion curve for an interactive view controller transition.
