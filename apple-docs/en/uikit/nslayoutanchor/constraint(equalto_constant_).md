---
title: 'constraint(equalTo:constant:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutanchor/constraint(equalto:constant:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutanchor/constraint(equalto:constant:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutanchor/constraint%28equalto%3Aconstant%3A%29.json'
content_hash: 'sha256:1433eade9c4841ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutAnchor](../nslayoutanchor.md)

# constraint(equalTo:constant:)

<sub>Instance Method</sub>

Returns a constraint that defines one item’s attribute as equal to another item’s attribute plus a constant offset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraint(equalTo anchor: NSLayoutAnchor<AnchorType>, constant c: CGFloat) -> NSLayoutConstraint
```

## Parameters

- `anchor` — A layout anchor from a [UIView](../uiview.md), [NSView](../../appkit/nsview.md), or [UILayoutGuide](../uilayoutguide.md) object. You must use a subclass of [NSLayoutAnchor](../nslayoutanchor.md) that matches the current anchor. For example, if you call this method on an [NSLayoutXAxisAnchor](../nslayoutxaxisanchor.md) object, this parameter must be another [NSLayoutXAxisAnchor](../nslayoutxaxisanchor.md).

- `c` — The constant offset for the constraint.

## Return Value

An [NSLayoutConstraint](../nslayoutconstraint.md) object that defines an equal relationship between the attributes represented by the two layout anchors plus a constant offset.

## Discussion

This method defines the relationship `first attribute = second attribute + c`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter. The value `c`, represents a constant offset. All values are measured in points; however, these values can be interpreted in different ways, depending on the type of layout anchor.

- For [NSLayoutXAxisAnchor](../nslayoutxaxisanchor.md) objects, the first attribute is positioned `c` points after the second attribute. When using leading or trailing attributes, values increase as you move in the language’s reading direction. In English, for example, values increase as you move to the right. For left and right attributes, values always increase as you move right.
- For [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md) objects, the first attribute is positioned `c` points below the second attribute. Values increase as you move down.
- For [NSLayoutDimension](../nslayoutdimension.md) objects, the size of the first attribute is `c` points larger than the size of the second attribute. Values increase as items increase in size.

The constraints produced by the following two examples are identical.

**Swift**

```swift
// Creating a constraint using NSLayoutConstraint
 
NSLayoutConstraint(item: textField,
                   attribute: .Leading,
                   relatedBy: .Equal,
                   toItem: label,
                   attribute: .Trailing,
                   multiplier: 1.0,
                   constant: 8.0).isActive = true
 
// Creating the same constraint using constraintEqualToAnchor:constant:
textField.leadingAnchor.constraintEqualToAnchor(label.trailingAnchor, constant: 8.0).isActive = true
```

**Objective-C**

```objc
// Creating a constraint using NSLayoutConstraint
 
[NSLayoutConstraint constraintWithItem:self.textField
                             attribute:NSLayoutAttributeLeading
                             relatedBy:NSLayoutRelationEqual
                                toItem:self.label
                             attribute:NSLayoutAttributeTrailing
                            multiplier:1.0
                              constant:8.0].active = YES;
 
// Creating the same constraint using constraintEqualToAnchor:constant:
[self.textField.leadingAnchor constraintEqualToAnchor:self.label.trailingAnchor constant:8.0].active = YES;
```

## See Also

### Building constraints

- [- constraintEqualToAnchor:](<constraint(equalto_).md>) — Returns a constraint that defines one item’s attribute as equal to another.
- [- constraintGreaterThanOrEqualToAnchor:](<constraint(greaterthanorequalto_).md>) — Returns a constraint that defines one item’s attribute as greater than or equal to another.
- [- constraintGreaterThanOrEqualToAnchor:constant:](<constraint(greaterthanorequalto_constant_).md>) — Returns a constraint that defines one item’s attribute as greater than or equal to another item’s attribute plus a constant offset.
- [- constraintLessThanOrEqualToAnchor:](<constraint(lessthanorequalto_).md>) — Returns a constraint that defines one item’s attribute as less than or equal to another.
- [- constraintLessThanOrEqualToAnchor:constant:](<constraint(lessthanorequalto_constant_).md>) — Returns a constraint that defines one item’s attribute as less than or equal to another item’s attribute plus a constant offset.
