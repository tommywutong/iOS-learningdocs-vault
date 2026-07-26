---
title: priority
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/priority
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/priority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/priority.json'
content_hash: 'sha256:0a2b7fa249ef3960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# priority

<sub>Instance Property</sub>

The priority of the constraint.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var priority: UILayoutPriority { get set }
```

## Discussion

By default, all constraints are required; this property is set to [required](../../appkit/nslayoutconstraint/priority-swift.struct/required.md) in macOS or `UILayoutPriorityRequired` in iOS.

If a constraint’s priority level is less than [required](../../appkit/nslayoutconstraint/priority-swift.struct/required.md) in macOS or `UILayoutPriorityRequired` in iOS, then it is optional. Higher priority constraints are satisfied before lower priority constraints; however, optional constraint satisfaction is not all or nothing. If a constraint `a == b` is optional, the constraint-based layout system will attempt to minimize `abs(a-b)`.

Priorities may not change from nonrequired to required, or from required to nonrequired. An exception will be thrown if a priority of [required](../../appkit/nslayoutconstraint/priority-swift.struct/required.md) in macOS or `UILayoutPriorityRequired` in iOS is changed to a lower priority, or if a lower priority is changed to a required priority after the constraints is added to a view. Changing from one optional priority to another optional priority is allowed even after the constraint is installed on a view.

Priorities must be greater than 0 and less than or equal to [required](../../appkit/nslayoutconstraint/priority-swift.struct/required.md) in macOS or `UILayoutPriorityRequired` in iOS.

## See Also

### Getting the layout priority

- [UILayoutPriority](../uilayoutpriority.md) — The layout priority is used to indicate to the constraint-based layout system which constraints are more important, allowing the system to make appropriate tradeoffs when satisfying the constraints of the system as a whole.
- [NSLayoutConstraint.Priority](../../appkit/nslayoutconstraint/priority-swift.struct.md) — Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.
