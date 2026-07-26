---
title: 'constraint(greaterThanOrEqualToSystemSpacingBelow:multiplier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutyaxisanchor/constraint(greaterthanorequaltosystemspacingbelow:multiplier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor/constraint(greaterthanorequaltosystemspacingbelow:multiplier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutyaxisanchor/constraint%28greaterthanorequaltosystemspacingbelow%3Amultiplier%3A%29.json'
content_hash: 'sha256:6c932ca5327b3eb4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md)

# constraint(greaterThanOrEqualToSystemSpacingBelow:multiplier:)

<sub>Instance Method</sub>

Returns a constraint that defines the minimum distance by which the current anchor is positioned below the specified anchor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraint(greaterThanOrEqualToSystemSpacingBelow anchor: NSLayoutYAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint
```

## Parameters

- `anchor` — The anchor to use as the starting point for the constraint.

- `multiplier` — The multiple of the system spacing to use as the distance between the two anchors.

## Return Value

An [NSLayoutConstraint](../nslayoutconstraint.md) object that imposes a minimum distance between the current anchor and the object in the `anchor` parameter.

## Discussion

The constraint causes the current anchor to be positioned below the object in the `anchor` parameter. The minimum distance between the two anchors is determined by multiplying the system spacing by the value in the `multiplier` parameter. The value of the system spacing is determined from information available from the anchors. For example, if the anchors represent text baselines, the spacing is determined by the fonts used at those baselines.

## See Also

### Building system spacing constraints

- [- constraintEqualToSystemSpacingBelowAnchor:multiplier:](<constraint(equaltosystemspacingbelow_multiplier_).md>) — Returns a constraint that defines the specific distance at which the current anchor is positioned below the specified anchor.
- [- constraintLessThanOrEqualToSystemSpacingBelowAnchor:multiplier:](<constraint(lessthanorequaltosystemspacingbelow_multiplier_).md>) — Returns a constraint that defines the maximum distance by which the current anchor is positioned below the specified anchor.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
