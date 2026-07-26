---
title: 'constraint(equalToSystemSpacingAfter:multiplier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutxaxisanchor/constraint(equaltosystemspacingafter:multiplier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutxaxisanchor/constraint(equaltosystemspacingafter:multiplier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutxaxisanchor/constraint%28equaltosystemspacingafter%3Amultiplier%3A%29.json'
content_hash: 'sha256:0df0ad6cfb592612'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutXAxisAnchor](../nslayoutxaxisanchor.md)

# constraint(equalToSystemSpacingAfter:multiplier:)

<sub>Instance Method</sub>

Returns a constraint that defines by how much the current anchor trails the specified anchor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraint(equalToSystemSpacingAfter anchor: NSLayoutXAxisAnchor, multiplier: CGFloat) -> NSLayoutConstraint
```

## Parameters

- `anchor` — The anchor to use as the starting point for the constraint.

- `multiplier` — The multiple of the system spacing to use as the distance between the two anchors.

## Return Value

An [NSLayoutConstraint](../nslayoutconstraint.md) object that imposes a specific distance between the current anchor and the object in the `anchor` parameter.

## Discussion

The constraint causes the current anchor to trail the object in the `anchor` parameter. For example, in a left-to-right layout, the current anchor is to the right of `anchor`, but in a right-to-left layout, it’s to the left of `anchor`.

The distance between the two anchors is determined by multiplying the system spacing by the value in the `multiplier` parameter. The value of the system space is determined from information available from the anchors.

## See Also

### Building system spacing constraints

- [- constraintGreaterThanOrEqualToSystemSpacingAfterAnchor:multiplier:](<constraint(greaterthanorequaltosystemspacingafter_multiplier_).md>) — Returns a constraint that defines the minimum amount by which the current anchor trails the specified anchor.
- [- constraintLessThanOrEqualToSystemSpacingAfterAnchor:multiplier:](<constraint(lessthanorequaltosystemspacingafter_multiplier_).md>) — Returns a constraint that defines the maximum amount by which the current anchor trails the specified anchor.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
