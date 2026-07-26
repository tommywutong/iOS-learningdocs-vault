---
title: isLayoutMarginsRelativeArrangement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/islayoutmarginsrelativearrangement
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/islayoutmarginsrelativearrangement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/islayoutmarginsrelativearrangement.json'
content_hash: 'sha256:923772972524cd89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# isLayoutMarginsRelativeArrangement

<sub>Instance Property</sub>

A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isLayoutMarginsRelativeArrangement: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the stack view will layout its arranged views relative to its layout margins. If [false](../../swift/false.md), it lays out the arranged views relative to its bounds. The default is [false](../../swift/false.md).

## See Also

### Configuring the layout

- [axis](axis.md) — The axis along which the arranged views lay out.
- [alignment](alignment-swift.property.md) — The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [distribution](distribution-swift.property.md) — The distribution of the arranged views along the stack view’s axis.
- [spacing](spacing.md) — The distance in points between the adjacent edges of the stack view’s arranged views.
- [baselineRelativeArrangement](isbaselinerelativearrangement.md) — A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
