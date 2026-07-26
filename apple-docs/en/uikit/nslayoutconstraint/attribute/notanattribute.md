---
title: NSLayoutConstraint.Attribute.notAnAttribute
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutconstraint/attribute/notanattribute
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutconstraint/attribute/notanattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutconstraint/attribute/notanattribute.json'
content_hash: 'sha256:88ac16a3a741ab5a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSLayoutConstraint](../../nslayoutconstraint.md) · [Attribute](../attribute.md)

# NSLayoutConstraint.Attribute.notAnAttribute

<sub>Case</sub>

A placeholder value for indicating that the constraint’s second item and second attribute aren’t used in any calculations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case notAnAttribute
```

## Discussion

Use this value when creating a constraint that assigns a constant to an attribute. For example, `item1.height >= 40`. If a constraint only has one item, set the second item to `nil`, and set the second attribute to [NSLayoutAttributeNotAnAttribute](notanattribute.md).

## See Also

### Constants

- [NSLayoutAttributeLeft](left.md) — The left side of the object’s alignment rectangle.
- [NSLayoutAttributeRight](right.md) — The right side of the object’s alignment rectangle.
- [NSLayoutAttributeTop](top.md) — The top of the object’s alignment rectangle.
- [NSLayoutAttributeBottom](bottom.md) — The bottom of the object’s alignment rectangle.
- [NSLayoutAttributeLeading](leading.md) — The leading edge of the object’s alignment rectangle.
- [NSLayoutAttributeTrailing](trailing.md) — The trailing edge of the object’s alignment rectangle.
- [NSLayoutAttributeWidth](width.md) — The width of the object’s alignment rectangle.
- [NSLayoutAttributeHeight](height.md) — The height of the object’s alignment rectangle.
- [NSLayoutAttributeCenterX](centerx.md) — The center along the x-axis of the object’s alignment rectangle.
- [NSLayoutAttributeCenterY](centery.md) — The center along the y-axis of the object’s alignment rectangle.
- [NSLayoutAttributeLastBaseline](lastbaseline.md) — The object’s baseline.
- [NSLayoutAttributeFirstBaseline](firstbaseline.md) — The object’s baseline.
- [NSLayoutAttributeLeftMargin](leftmargin.md) — The object’s left margin.
- [NSLayoutAttributeRightMargin](rightmargin.md) — The object’s right margin.
- [NSLayoutAttributeTopMargin](topmargin.md) — The object’s top margin.
