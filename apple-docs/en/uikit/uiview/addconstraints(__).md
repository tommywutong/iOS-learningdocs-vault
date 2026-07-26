---
title: 'addConstraints(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/addconstraints(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/addconstraints(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/addconstraints%28_%3A%29.json'
content_hash: 'sha256:1e48b3a40929ce21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# addConstraints(_:)

<sub>Instance Method</sub>

Adds multiple constraints on the layout of the receiving view or its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addConstraints(_ constraints: [NSLayoutConstraint])
```

## Parameters

- `constraints` — An array of constraints to be added to the view. All constraints may only reference the view itself or its subviews.

## Discussion

All constraints must involve only views that are within scope of the receiving view. Specifically, any views involved must be either the receiving view itself, or a subview of the receiving view. Constraints that are added to a view are said to be held by that view. The coordinate system used when evaluating each constraint is the coordinate system of the view that holds the constraint.

When developing for iOS 8.0 or later, use the [NSLayoutConstraint](../nslayoutconstraint.md) class’s  [+ activateConstraints:](<../nslayoutconstraint/activate(__).md>) method instead of calling the [- addConstraints:](<addconstraints(__).md>) method directly. The [+ activateConstraints:](<../nslayoutconstraint/activate(__).md>) method automatically adds the constraints to the correct views.

## See Also

### Managing the view’s constraints

- [constraints](constraints.md) — The constraints held by the view.
- [- addConstraint:](<addconstraint(__).md>) — Adds a constraint on the layout of the receiving view or its subviews.
- [- removeConstraint:](<removeconstraint(__).md>) — Removes the specified constraint from the view.
- [- removeConstraints:](<removeconstraints(__).md>) — Removes the specified constraints from the view.
