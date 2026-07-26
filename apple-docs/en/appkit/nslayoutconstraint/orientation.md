---
title: NSLayoutConstraint.Orientation
framework: AppKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutconstraint/orientation
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutconstraint/orientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutconstraint/orientation.json'
content_hash: 'sha256:5ed901595c7e92f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# NSLayoutConstraint.Orientation

<sub>Enumeration</sub>

The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.

<sub>macOS</sub>

```swift
enum Orientation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLayoutConstraintOrientationHorizontal](orientation/horizontal.md) — The constraint orientation applied to laying out the horizontal relationship between objects.
- [NSLayoutConstraintOrientationVertical](orientation/vertical.md) — The constraint orientation applied to laying out the vertical relationship between objects.

### Initializers

- [init(rawValue:)](<orientation/init(rawvalue_).md>)

## See Also

### Constants

- [Relation](relation-swift.enum.md) — The relation between the first attribute and the modified second attribute in a constraint.
- [Attribute](attribute.md) — The part of the object’s visual representation that should be used to get the value for the constraint.
- [FormatOptions](formatoptions.md) — A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSEdgeInsets](../../foundation/nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
