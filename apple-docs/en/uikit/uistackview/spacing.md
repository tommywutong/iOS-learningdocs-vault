---
title: spacing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/spacing
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/spacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/spacing.json'
content_hash: 'sha256:47e9de392d256500'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# spacing

<sub>Instance Property</sub>

The distance in points between the adjacent edges of the stack view’s arranged views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var spacing: CGFloat { get set }
```

## Discussion

This property defines a strict spacing between arranged views for the [UIStackViewDistributionFillProportionally](distribution-swift.enum/fillproportionally.md) distributions. It represents the minimum spacing for the [UIStackViewDistributionEqualSpacing](distribution-swift.enum/equalspacing.md) and [UIStackViewDistributionEqualCentering](distribution-swift.enum/equalcentering.md) distributions. Use negative values to allow overlap. The default value is `0.0`.

## See Also

### Configuring the layout

- [axis](axis.md) — The axis along which the arranged views lay out.
- [alignment](alignment-swift.property.md) — The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [distribution](distribution-swift.property.md) — The distribution of the arranged views along the stack view’s axis.
- [baselineRelativeArrangement](isbaselinerelativearrangement.md) — A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
- [layoutMarginsRelativeArrangement](islayoutmarginsrelativearrangement.md) — A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.
