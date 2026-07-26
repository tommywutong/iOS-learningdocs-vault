---
title: NSLayoutConstraint.Relation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/relation-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/relation-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/relation-swift.enum.json'
content_hash: 'sha256:de301856a354d8f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# NSLayoutConstraint.Relation

<sub>Enumeration</sub>

The relation between the first attribute and the modified second attribute in a constraint.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Relation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLayoutRelationLessThanOrEqual](relation-swift.enum/lessthanorequal.md) — The constraint requires the first attribute to be less than or equal to the modified second attribute.
- [NSLayoutRelationEqual](relation-swift.enum/equal.md) — The constraint requires the first attribute to be exactly equal to the modified second attribute.
- [NSLayoutRelationGreaterThanOrEqual](relation-swift.enum/greaterthanorequal.md) — The constraint requires the first attribute to be greater than or equal to the modified second attribute.

### Initializers

- [init(rawValue:)](<relation-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [Attribute](attribute.md) — The part of the object’s visual representation that should be used to get the value for the constraint.
- [FormatOptions](formatoptions.md) — A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](../../appkit/nslayoutconstraint/orientation.md) — The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [Axis](axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [NSEdgeInsets](../../foundation/nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
- [NSLAYOUTCONSTRAINT_H](../nslayoutconstraint_h.md)
