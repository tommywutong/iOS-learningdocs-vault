---
title: isBaselineRelativeArrangement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/isbaselinerelativearrangement
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/isbaselinerelativearrangement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/isbaselinerelativearrangement.json'
content_hash: 'sha256:e3d73c27c08bad03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# isBaselineRelativeArrangement

<sub>Instance Property</sub>

A Boolean value that determines whether the vertical spacing between views is measured from their baselines.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isBaselineRelativeArrangement: Bool { get set }
```

## Discussion

If YES, the vertical space between views are measured from the last baseline of a text-based view, to the first baseline of the view below it. Top and bottom views are also positioned so that their closest baseline is the specified distance away from the stack view’s edge. This property is only used by vertical stack views. Use the [alignment](alignment-swift.property.md) property to baseline align views in a horizontal stack view.

The default value is [false](../../swift/false.md).

## See Also

### Configuring the layout

- [axis](axis.md) — The axis along which the arranged views lay out.
- [alignment](alignment-swift.property.md) — The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [distribution](distribution-swift.property.md) — The distribution of the arranged views along the stack view’s axis.
- [spacing](spacing.md) — The distance in points between the adjacent edges of the stack view’s arranged views.
- [layoutMarginsRelativeArrangement](islayoutmarginsrelativearrangement.md) — A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.
