---
title: axis
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/axis
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/axis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/axis.json'
content_hash: 'sha256:37cd383b853a63bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# axis

<sub>Instance Property</sub>

The axis along which the arranged views lay out.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var axis: NSLayoutConstraint.Axis { get set }
```

## Discussion

This property determines the orientation of the arranged views. Assigning the [UILayoutConstraintAxisVertical](../nslayoutconstraint/axis/vertical.md) value creates a column of views. Assigning the [UILayoutConstraintAxisHorizontal](../nslayoutconstraint/axis/horizontal.md) value creates a row. The default value is [UILayoutConstraintAxisHorizontal](../nslayoutconstraint/axis/horizontal.md).

## See Also

### Configuring the layout

- [alignment](alignment-swift.property.md) — The alignment of the arranged subviews perpendicular to the stack view’s axis.
- [distribution](distribution-swift.property.md) — The distribution of the arranged views along the stack view’s axis.
- [spacing](spacing.md) — The distance in points between the adjacent edges of the stack view’s arranged views.
- [baselineRelativeArrangement](isbaselinerelativearrangement.md) — A Boolean value that determines whether the vertical spacing between views is measured from their baselines.
- [layoutMarginsRelativeArrangement](islayoutmarginsrelativearrangement.md) — A Boolean value that determines whether the stack view lays out its arranged views relative to its layout margins.
