---
title: alignmentRectProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectprovider.json'
content_hash: 'sha256:2cba8a811a369953'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIViewController](../../../uiviewcontroller.md) · [Transition](../../transition.md) · [ZoomOptions](../zoomoptions.md)

# alignmentRectProvider

<sub>Instance Property</sub>

A closure that returns the alignment rectangle for the starting and ending views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)? { get set }
```

## See Also

### Setting options

- [AlignmentRectContext](alignmentrectcontext.md) — An object that contains a zoom transition’s starting and ending views.
- [dimmingColor](dimmingcolor.md) — The dimming color.
- [dimmingVisualEffect](dimmingvisualeffect.md) — The dimming visual effect.
