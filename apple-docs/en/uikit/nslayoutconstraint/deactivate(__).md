---
title: 'deactivate(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutconstraint/deactivate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/deactivate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/deactivate%28_%3A%29.json'
content_hash: 'sha256:13977242dcbfbdcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# deactivate(_:)

<sub>Type Method</sub>

Deactivates each constraint in the specified array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func deactivate(_ constraints: [NSLayoutConstraint])
```

## Parameters

- `constraints` — An array of constraints to deactivate.

## Discussion

This is a convenience method that provides an easy way to deactivate a set of constraints with one call. The effect of this method is the same as setting the [active](isactive.md) property of each constraint to [false](../../swift/false.md). Typically, using this method is more efficient than deactivating each constraint individually.

## See Also

### Activating and deactivating constraints

- [active](isactive.md) — The active state of the constraint.
- [+ activateConstraints:](<activate(__).md>) — Activates each constraint in the specified array.
