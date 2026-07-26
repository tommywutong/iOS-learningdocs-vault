---
title: alignmentRectProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uizoomtransitionoptions/alignmentrectprovider
source_url: 'https://developer.apple.com/documentation/uikit/uizoomtransitionoptions/alignmentrectprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uizoomtransitionoptions/alignmentrectprovider.json'
content_hash: 'sha256:e7a48dff040193ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [ZoomOptions](../uiviewcontroller/transition/zoomoptions.md)

# alignmentRectProvider

<sub>Instance Property</sub>

A block that returns the alignment rectangle for the starting and ending views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) struct CGRect (^)(UIZoomTransitionAlignmentRectContext *) alignmentRectProvider;
```

## See Also

### Setting options

- [AlignmentRectContext](../uiviewcontroller/transition/zoomoptions/alignmentrectcontext.md) — An object that contains a zoom transition’s starting and ending views.
- [dimmingColor](../uiviewcontroller/transition/zoomoptions/dimmingcolor.md) — The dimming color.
- [dimmingVisualEffect](../uiviewcontroller/transition/zoomoptions/dimmingvisualeffect.md) — The dimming visual effect.
