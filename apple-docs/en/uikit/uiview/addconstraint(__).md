---
title: 'addConstraint(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/addconstraint(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/addconstraint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/addconstraint%28_%3A%29.json'
content_hash: 'sha256:6b0dea5019d491dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# addConstraint(_:)

<sub>Instance Method</sub>

Adds a constraint on the layout of the receiving view or its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addConstraint(_ constraint: NSLayoutConstraint)
```

## Parameters

- `constraint` — The constraint to be added to the view. The constraint may only reference the view itself or its subviews.

## Discussion

The constraint must involve only views that are within scope of the receiving view. Specifically, any views involved must be either the receiving view itself, or a subview of the receiving view. Constraints that are added to a view are said to be held by that view. The coordinate system used when evaluating the constraint is the coordinate system of the view that holds the constraint.

When developing for iOS 8.0 or later, set the constraint’s [active](../nslayoutconstraint/isactive.md) property to [true](../../swift/true.md) instead of calling the [- addConstraint:](<addconstraint(__).md>) method directly. The [active](../nslayoutconstraint/isactive.md) property automatically adds and removes the constraint from the correct view.

## See Also

### Managing the view’s constraints

- [constraints](constraints.md) — The constraints held by the view.
- [- addConstraints:](<addconstraints(__).md>) — Adds multiple constraints on the layout of the receiving view or its subviews.
- [- removeConstraint:](<removeconstraint(__).md>) — Removes the specified constraint from the view.
- [- removeConstraints:](<removeconstraints(__).md>) — Removes the specified constraints from the view.
