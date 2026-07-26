---
title: 'removeConstraints(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/removeconstraints(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/removeconstraints(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/removeconstraints%28_%3A%29.json'
content_hash: 'sha256:fc3ac2a4beba996b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# removeConstraints(_:)

<sub>Instance Method</sub>

Removes the specified constraints from the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeConstraints(_ constraints: [NSLayoutConstraint])
```

## Parameters

- `constraints` — The constraints to remove.

## Discussion

When developing for iOS 8.0 or later, use the [NSLayoutConstraint](../nslayoutconstraint.md) class’s  [+ deactivateConstraints:](<../nslayoutconstraint/deactivate(__).md>) method instead of calling the [- removeConstraints:](<removeconstraints(__).md>) method directly. The [+ deactivateConstraints:](<../nslayoutconstraint/deactivate(__).md>) method automatically removes the constraints from the correct views.

## See Also

### Managing the view’s constraints

- [constraints](constraints.md) — The constraints held by the view.
- [- addConstraint:](<addconstraint(__).md>) — Adds a constraint on the layout of the receiving view or its subviews.
- [- addConstraints:](<addconstraints(__).md>) — Adds multiple constraints on the layout of the receiving view or its subviews.
- [- removeConstraint:](<removeconstraint(__).md>) — Removes the specified constraint from the view.
