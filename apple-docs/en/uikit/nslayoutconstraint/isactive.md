---
title: isActive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/isactive
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/isactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/isactive.json'
content_hash: 'sha256:b4cf8dcc80743ba5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# isActive

<sub>Instance Property</sub>

The active state of the constraint.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isActive: Bool { get set }
```

## Discussion

You can activate or deactivate a constraint by changing this property. Note that only active constraints affect the calculated layout. If you try to activate a constraint whose items have no common ancestor, an exception is thrown. For newly created constraints, the [active](isactive.md) property is [false](../../swift/false.md) by default.

Activating or deactivating the constraint calls [- addConstraint:](<../uiview/addconstraint(__).md>) and [- removeConstraint:](<../uiview/removeconstraint(__).md>) on the view that is the closest common ancestor of the items managed by this constraint. Use this property instead of calling [- addConstraint:](<../uiview/addconstraint(__).md>) or [- removeConstraint:](<../uiview/removeconstraint(__).md>) directly.

## See Also

### Activating and deactivating constraints

- [+ activateConstraints:](<activate(__).md>) — Activates each constraint in the specified array.
- [+ deactivateConstraints:](<deactivate(__).md>) — Deactivates each constraint in the specified array.
