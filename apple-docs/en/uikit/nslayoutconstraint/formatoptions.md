---
title: NSLayoutConstraint.FormatOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/formatoptions
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/formatoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/formatoptions.json'
content_hash: 'sha256:5afae44342c6a299'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# NSLayoutConstraint.FormatOptions

<sub>Structure</sub>

A bit mask that specifies both a part of an interface element to align and a direction for the alignment between two interface elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct FormatOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSLayoutFormatAlignAllLeft](formatoptions/alignallleft.md) — Align all specified interface elements using [NSLayoutAttributeLeft](attribute/left.md) on each.
- [NSLayoutFormatAlignAllRight](formatoptions/alignallright.md) — Align all specified interface elements using [NSLayoutAttributeRight](attribute/right.md) on each.
- [NSLayoutFormatAlignAllTop](formatoptions/alignalltop.md) — Align all specified interface elements using [NSLayoutAttributeTop](attribute/top.md) on each.
- [NSLayoutFormatAlignAllBottom](formatoptions/alignallbottom.md) — Align all specified interface elements using [NSLayoutAttributeBottom](attribute/bottom.md) on each.
- [NSLayoutFormatAlignAllLeading](formatoptions/alignallleading.md) — Align all specified interface elements using [NSLayoutAttributeLeading](attribute/leading.md) on each.
- [NSLayoutFormatAlignAllTrailing](formatoptions/alignalltrailing.md) — Align all specified interface elements using [NSLayoutAttributeTrailing](attribute/trailing.md) on each.
- [NSLayoutFormatAlignAllCenterX](formatoptions/alignallcenterx.md) — Align all specified interface elements using [NSLayoutAttributeCenterX](attribute/centerx.md) on each.
- [NSLayoutFormatAlignAllCenterY](formatoptions/alignallcentery.md) — Align all specified interface elements using [NSLayoutAttributeCenterY](attribute/centery.md) on each.
- [NSLayoutFormatAlignAllLastBaseline](formatoptions/alignalllastbaseline.md) — Align all specified interface elements using the last baseline of each one.
- [NSLayoutFormatAlignAllFirstBaseline](formatoptions/alignallfirstbaseline.md) — Align all specified interface elements using the first baseline of each one.
- [NSLayoutFormatAlignmentMask](formatoptions/alignmentmask.md) — Bit mask that can be combined with a [FormatOptions](formatoptions.md) variable to yield only the alignment portion of the format options.
- [NSLayoutFormatDirectionLeadingToTrailing](formatoptions/directionleadingtotrailing.md) — Arrange objects in order based on the normal text flow for the current user interface language. In left-to-right languages (like English), this arrangement results in the first object being placed farthest to the left, the next one to its right, and so on. In right-to-left languages (like Arabic or Hebrew), the ordering is reversed.
- [NSLayoutFormatDirectionLeftToRight](formatoptions/directionlefttoright.md) — Arrange objects in order from left to right.
- [NSLayoutFormatDirectionRightToLeft](formatoptions/directionrighttoleft.md) — Arrange objects in order from right to left.
- [NSLayoutFormatDirectionMask](formatoptions/directionmask.md) — A bit mask that can be combined with an [FormatOptions](formatoptions.md) variable to yield only the direction portion of the format options.
- [NSLayoutFormatSpacingBaselineToBaseline](formatoptions/spacingbaselinetobaseline.md) — Align elements vertically according to their baseline positions.
- [NSLayoutFormatSpacingMask](formatoptions/spacingmask.md) — A bit mask that can be combined with an [FormatOptions](formatoptions.md) variable to yield only the spacing baseline spacing portion of the format options.

### Initializers

- [init(rawValue:)](<formatoptions/init(rawvalue_).md>) — Creates a formatting-options structure with the specified raw value.

## See Also

### Constants

- [Relation](relation-swift.enum.md) — The relation between the first attribute and the modified second attribute in a constraint.
- [Attribute](attribute.md) — The part of the object’s visual representation that should be used to get the value for the constraint.
- [NSLayoutConstraint.Orientation](../../appkit/nslayoutconstraint/orientation.md) — The layout constraint orientation, either horizontal or vertical, that the constraint uses to enforce layout between objects.
- [Axis](axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [NSEdgeInsets](../../foundation/nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
- [NSLAYOUTCONSTRAINT_H](../nslayoutconstraint_h.md)
