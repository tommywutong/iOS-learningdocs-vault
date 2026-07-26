---
title: 'constraint(equalTo:multiplier:constant:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutdimension/constraint(equalto:multiplier:constant:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutdimension/constraint(equalto:multiplier:constant:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutdimension/constraint%28equalto%3Amultiplier%3Aconstant%3A%29.json'
content_hash: 'sha256:4a860d48eee3a905'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutDimension](../nslayoutdimension.md)

# constraint(equalTo:multiplier:constant:)

<sub>Instance Method</sub>

Returns a constraint that defines the anchor’s size attribute as equal to the specified size attribute multiplied by a constant plus an offset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraint(equalTo anchor: NSLayoutDimension, multiplier m: CGFloat, constant c: CGFloat) -> NSLayoutConstraint
```

## Parameters

- `anchor` — A dimension anchor from a [UIView](../uiview.md), [NSView](../../appkit/nsview.md), or [UILayoutGuide](../uilayoutguide.md) object.

- `m` — The multiplier constant for the constraint.

- `c` — The offset constant for this relationship.

## Return Value

An [NSLayoutConstraint](../nslayoutconstraint.md) object that defines the attribute represented by this layout anchor as equal to the attribute represented by the `anchor` parameter multiplied by the `m` constant plus the constant `c`.

## Discussion

This method defines the relationship `first attribute = (m * second attribute) + c`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter.

The constraints produced by the following two examples are identical.

**Swift**

```swift
// Creating a constraint using NSLayoutConstraint
NSLayoutConstraint(item: button,
                   attribute: .Width,
                   relatedBy: .Equal,
                   toItem: button,
                   attribute: .Height,
                   multiplier: 2.0,
                   constant: 40.0).isActive = true
 
// Creating the same constraint using constraintEqualToAnchor:multiplier:constant:
button.widthAnchor.constraintEqualToAnchor(button.heightAnchor, multiplier: 2.0, constant: 40.0).isActive = true
```

**Objective-C**

```objc
// Creating a constraint using NSLayoutConstraint
[NSLayoutConstraint
 constraintWithItem:self.button
 attribute:NSLayoutAttributeWidth
 relatedBy:NSLayoutRelationEqual
 toItem:self.button
 attribute:NSLayoutAttributeHeight
 multiplier:2.0
 constant:40.0].active = YES;
 
// Creating the same constraint using constraintEqualToAnchor:multiplier:constant:
[self.button.widthAnchor constraintEqualToAnchor:self.button.heightAnchor multiplier:2.0 constant: 40.0].active = YES;
```

## See Also

### Building constraints

- [- constraintEqualToAnchor:multiplier:](<constraint(equalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.
- [- constraintEqualToConstant:](<constraint(equaltoconstant_).md>) — Returns a constraint that defines a constant size for the anchor’s size attribute.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:](<constraint(greaterthanorequalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:constant:](<constraint(greaterthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintGreaterThanOrEqualToConstant:](<constraint(greaterthanorequaltoconstant_).md>) — Returns a constraint that defines the minimum size for the anchor’s size attribute.
- [- constraintLessThanOrEqualToAnchor:multiplier:](<constraint(lessthanorequalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as less than or equal to the specified anchor multiplied by the constant.
- [- constraintLessThanOrEqualToAnchor:multiplier:constant:](<constraint(lessthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintLessThanOrEqualToConstant:](<constraint(lessthanorequaltoconstant_).md>) — Returns a constraint that defines the maximum size for the anchor’s size attribute.
