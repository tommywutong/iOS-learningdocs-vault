---
title: NSLayoutConstraint.Axis
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/axis
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/axis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/axis.json'
content_hash: 'sha256:12b87fb0323fb122'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# NSLayoutConstraint.Axis

<sub>Enumeration</sub>

Keys that specify a horizontal or vertical layout constraint between objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Axis
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UILayoutConstraintAxisHorizontal](axis/horizontal.md) — The constraint applied when laying out the horizontal relationship between objects.
- [UILayoutConstraintAxisVertical](axis/vertical.md) — The constraint applied when laying out the vertical relationship between objects.

### Initializers

- [init(rawValue:)](<axis/init(rawvalue_).md>)

## See Also

### Constants

- [Relation](relation-swift.enum.md) — The relation between the first attribute and the modified second attribute in a constraint.
- [Attribute](attribute.md) — The part of the object’s visual representation that should be used to get the value for the constraint.
- [FormatOptions](formatoptions.md) — A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](../../appkit/nslayoutconstraint/orientation.md) — The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [NSEdgeInsets](../../foundation/nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
- [NSLAYOUTCONSTRAINT_H](../nslayoutconstraint_h.md)
