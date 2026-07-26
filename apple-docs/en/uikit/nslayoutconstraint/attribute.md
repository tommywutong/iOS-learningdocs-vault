---
title: NSLayoutConstraint.Attribute
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/attribute
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/attribute.json'
content_hash: 'sha256:75caf0596edb1075'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# NSLayoutConstraint.Attribute

<sub>Enumeration</sub>

The part of the object’s visual representation that should be used to get the value for the constraint.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Attribute
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLayoutAttributeLeft](attribute/left.md) — The left side of the object’s alignment rectangle.
- [NSLayoutAttributeRight](attribute/right.md) — The right side of the object’s alignment rectangle.
- [NSLayoutAttributeTop](attribute/top.md) — The top of the object’s alignment rectangle.
- [NSLayoutAttributeBottom](attribute/bottom.md) — The bottom of the object’s alignment rectangle.
- [NSLayoutAttributeLeading](attribute/leading.md) — The leading edge of the object’s alignment rectangle.
- [NSLayoutAttributeTrailing](attribute/trailing.md) — The trailing edge of the object’s alignment rectangle.
- [NSLayoutAttributeWidth](attribute/width.md) — The width of the object’s alignment rectangle.
- [NSLayoutAttributeHeight](attribute/height.md) — The height of the object’s alignment rectangle.
- [NSLayoutAttributeCenterX](attribute/centerx.md) — The center along the x-axis of the object’s alignment rectangle.
- [NSLayoutAttributeCenterY](attribute/centery.md) — The center along the y-axis of the object’s alignment rectangle.
- [NSLayoutAttributeLastBaseline](attribute/lastbaseline.md) — The object’s baseline.
- [NSLayoutAttributeFirstBaseline](attribute/firstbaseline.md) — The object’s baseline.
- [NSLayoutAttributeLeftMargin](attribute/leftmargin.md) — The object’s left margin.
- [NSLayoutAttributeRightMargin](attribute/rightmargin.md) — The object’s right margin.
- [NSLayoutAttributeTopMargin](attribute/topmargin.md) — The object’s top margin.
- [NSLayoutAttributeBottomMargin](attribute/bottommargin.md) — The object’s bottom margin.
- [NSLayoutAttributeLeadingMargin](attribute/leadingmargin.md) — The object’s leading margin.
- [NSLayoutAttributeTrailingMargin](attribute/trailingmargin.md) — The object’s trailing margin.
- [NSLayoutAttributeCenterXWithinMargins](attribute/centerxwithinmargins.md) — The center along the x-axis between the object’s left and right margin.
- [NSLayoutAttributeCenterYWithinMargins](attribute/centerywithinmargins.md) — The center along the y-axis between the object’s top and bottom margin.
- [NSLayoutAttributeNotAnAttribute](attribute/notanattribute.md) — A placeholder value for indicating that the constraint’s second item and second attribute aren’t used in any calculations.

### Initializers

- [init(rawValue:)](<attribute/init(rawvalue_).md>)

## See Also

### Constants

- [Relation](relation-swift.enum.md) — The relation between the first attribute and the modified second attribute in a constraint.
- [FormatOptions](formatoptions.md) — A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.
- [NSLayoutConstraint.Orientation](../../appkit/nslayoutconstraint/orientation.md) — The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [Axis](axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [NSEdgeInsets](../../foundation/nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
- [NSLAYOUTCONSTRAINT_H](../nslayoutconstraint_h.md)
