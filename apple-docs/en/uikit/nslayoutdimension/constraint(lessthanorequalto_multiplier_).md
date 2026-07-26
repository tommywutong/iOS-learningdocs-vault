---
title: 'constraint(lessThanOrEqualTo:multiplier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutdimension/constraint(lessthanorequalto:multiplier:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutdimension/constraint(lessthanorequalto:multiplier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutdimension/constraint%28lessthanorequalto%3Amultiplier%3A%29.json'
content_hash: 'sha256:dcd3967e32caa5ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutDimension](../nslayoutdimension.md)

# constraint(lessThanOrEqualTo:multiplier:)

<sub>Instance Method</sub>

Returns a constraint that defines the anchor’s size attribute as less than or equal to the specified anchor multiplied by the constant.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraint(lessThanOrEqualTo anchor: NSLayoutDimension, multiplier m: CGFloat) -> NSLayoutConstraint
```

## Parameters

- `anchor` — A dimension anchor from a [UIView](../uiview.md), [NSView](../../appkit/nsview.md), or [UILayoutGuide](../uilayoutguide.md) object.

- `m` — The multiplier constant for the constraint.

## Return Value

An [NSLayoutConstraint](../nslayoutconstraint.md) object that defines the attribute represented by this layout anchor as less than or equal to the attribute represented by the `anchor` parameter multiplied by the `m` constant.

## Discussion

This method defines the relationship `first attribute <= m * second attribute` . Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter.

The constraints produced by the following two examples are identical.

**Swift**

```swift
// Creating a constraint using NSLayoutConstraint
NSLayoutConstraint(item: saveButton,
                   attribute: .Width,
                   relatedBy: .LessThanOrEqual,
                   toItem: cancelButton,
                   attribute: .Width,
                   multiplier: 2.0,
                   constant: 0.0).isActive = true
 
// Creating the same constraint using constraintLessThanOrEqualToAnchor:multiplier:
saveButton.widthAnchor.constraintLessThanOrEqualToAnchor(cancelButton.widthAnchor, multiplier: 2.0).isActive = true
```

**Objective-C**

```objc
// Creating a constraint using NSLayoutConstraint
[NSLayoutConstraint
 constraintWithItem:self.saveButton
 attribute:NSLayoutAttributeWidth
 relatedBy:NSLayoutRelationLessThanOrEqual
 toItem:self.cancelButton
 attribute:NSLayoutAttributeWidth
 multiplier:2.0
 constant:0.0].active = YES;
 
// Creating the same constraint using constraintLessThanOrEqualToAnchor:multiplier:
[self.saveButton.widthAnchor constraintLessThanOrEqualToAnchor:self.cancelButton.widthAnchor multiplier:2.0].active = YES;
```

## See Also

### Building constraints

- [- constraintEqualToAnchor:multiplier:](<constraint(equalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.
- [- constraintEqualToAnchor:multiplier:constant:](<constraint(equalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as equal to the specified size attribute multiplied by a constant plus an offset.
- [- constraintEqualToConstant:](<constraint(equaltoconstant_).md>) — Returns a constraint that defines a constant size for the anchor’s size attribute.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:](<constraint(greaterthanorequalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:constant:](<constraint(greaterthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintGreaterThanOrEqualToConstant:](<constraint(greaterthanorequaltoconstant_).md>) — Returns a constraint that defines the minimum size for the anchor’s size attribute.
- [- constraintLessThanOrEqualToAnchor:multiplier:constant:](<constraint(lessthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintLessThanOrEqualToConstant:](<constraint(lessthanorequaltoconstant_).md>) — Returns a constraint that defines the maximum size for the anchor’s size attribute.
