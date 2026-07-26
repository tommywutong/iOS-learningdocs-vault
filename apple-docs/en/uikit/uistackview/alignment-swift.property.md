---
title: alignment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/alignment-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/alignment-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/alignment-swift.property.json'
content_hash: 'sha256:908bc2a94791a6fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# alignment

<sub>Instance Property</sub>

The alignment of the arranged subviews perpendicular to the stack view’s axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var alignment: UIStackView.Alignment { get set }
```

## Discussion

This property determines how the stack view lays out its arranged views perpendicularly to its axis. The default value is [UIStackViewAlignmentFill](alignment-swift.enum/fill.md). For a list of possible values, see [Alignment](alignment-swift.enum.md).

## See Also

### Configuring the layout

- [axis](axis.md) — The axis along which the arranged views lay out.
- [distribution](distribution-swift.property.md) — The distribution of the arranged views along the stack view’s axis.
- [spacing](spacing.md) — The distance in points between the adjacent edges of the stack view’s arranged views.
- [baselineRelativeArrangement](isbaselinerelativearrangement.md) — A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
- [layoutMarginsRelativeArrangement](islayoutmarginsrelativearrangement.md) — A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.
