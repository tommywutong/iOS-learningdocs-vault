---
title: shouldBeArchived
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/shouldbearchived
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/shouldbearchived'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/shouldbearchived.json'
content_hash: 'sha256:19468158170d38fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# shouldBeArchived

<sub>Instance Property</sub>

A Boolean value that determines whether the constraint should be archived by its owning view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shouldBeArchived: Bool { get set }
```

## Discussion

When a view is archived, it archives some but not all constraints in its [constraints](../uiview/constraints.md) array. The value of [shouldBeArchived](shouldbearchived.md) informs the view if a particular constraint should be archived by the view.

If a constraint is created at runtime in response to the state of the object, it isn’t appropriate to archive the constraint. Instead you archive the state that gives rise to the constraint. The default value for this property is [false](../../swift/false.md).
