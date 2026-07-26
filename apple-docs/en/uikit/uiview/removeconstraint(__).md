---
title: 'removeConstraint(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/removeconstraint(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/removeconstraint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/removeconstraint%28_%3A%29.json'
content_hash: 'sha256:9e598db2750c32e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# removeConstraint(_:)

<sub>Instance Method</sub>

Removes the specified constraint from the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeConstraint(_ constraint: NSLayoutConstraint)
```

## Parameters

- `constraint` — The constraint to remove. Removing a constraint not held by the view has no effect.

## Discussion

When developing for iOS 8.0 or later, set the constraint’s [active](../nslayoutconstraint/isactive.md) property to [false](../../swift/false.md) instead of calling the [- removeConstraint:](<removeconstraint(__).md>) method directly. The [active](../nslayoutconstraint/isactive.md) property automatically adds and removes the constraint from the correct view.

## See Also

### Managing the view’s constraints

- [constraints](constraints.md) — The constraints held by the view.
- [- addConstraint:](<addconstraint(__).md>) — Adds a constraint on the layout of the receiving view or its subviews.
- [- addConstraints:](<addconstraints(__).md>) — Adds multiple constraints on the layout of the receiving view or its subviews.
- [- removeConstraints:](<removeconstraints(__).md>) — Removes the specified constraints from the view.
