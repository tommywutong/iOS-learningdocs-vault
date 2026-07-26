---
title: 'activate(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutconstraint/activate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/activate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/activate%28_%3A%29.json'
content_hash: 'sha256:54624c6080e781d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# activate(_:)

<sub>Type Method</sub>

Activates each constraint in the specified array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func activate(_ constraints: [NSLayoutConstraint])
```

## Parameters

- `constraints` — An array of constraints to activate.

## Discussion

This convenience method provides an easy way to activate a set of constraints with one call. The effect of this method is the same as setting the [active](isactive.md) property of each constraint to [true](../../swift/true.md). Typically, using this method is more efficient than activating each constraint individually.

## See Also

### Activating and deactivating constraints

- [active](isactive.md) — The active state of the constraint.
- [+ deactivateConstraints:](<deactivate(__).md>) — Deactivates each constraint in the specified array.
