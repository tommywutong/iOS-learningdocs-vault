---
title: constant
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/constant
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/constant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/constant.json'
content_hash: 'sha256:11d4d71cf7e77638'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# constant

<sub>Instance Property</sub>

The constant added to the multiplied second attribute participating in the constraint.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var constant: CGFloat { get set }
```

## Discussion

Unlike the other properties, the constant can be modified after constraint creation. Setting the constant on an existing constraint performs much better than removing the constraint and adding a new one that’s exactly like the old except that it has a different constant.

## See Also

### Accessing constraint data

- [firstItem](firstitem.md) — The first object participating in the constraint.
- [firstAttribute](firstattribute.md) — The attribute of the first object participating in the constraint.
- [relation](relation-swift.property.md) — The relation between the two attributes in the constraint.
- [secondItem](seconditem.md) — The second object participating in the constraint.
- [secondAttribute](secondattribute.md) — The attribute of the second object participating in the constraint.
- [multiplier](multiplier.md) — The multiplier applied to the second attribute participating in the constraint.
- [firstAnchor](firstanchor.md) — The first anchor that defines the constraint.
- [secondAnchor](secondanchor.md) — The second anchor that defines the constraint.
