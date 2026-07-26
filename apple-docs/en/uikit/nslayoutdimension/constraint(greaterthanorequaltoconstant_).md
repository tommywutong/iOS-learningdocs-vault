---
title: 'constraint(greaterThanOrEqualToConstant:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutdimension/constraint(greaterthanorequaltoconstant:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutdimension/constraint(greaterthanorequaltoconstant:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutdimension/constraint%28greaterthanorequaltoconstant%3A%29.json'
content_hash: 'sha256:8072bb56af14ebc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutDimension](../nslayoutdimension.md)

# constraint(greaterThanOrEqualToConstant:)

<sub>Instance Method</sub>

Returns a constraint that defines the minimum size for the anchor’s size attribute.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraint(greaterThanOrEqualToConstant c: CGFloat) -> NSLayoutConstraint
```

## Parameters

- `c` — A constant representing the minimum size of the attribute associated with this dimension anchor.

## Return Value

An [NSLayoutConstraint](../nslayoutconstraint.md) object that defines a minimum size for the attribute associated with this dimension anchor.

## Discussion

This method defines the relationship `first attribute >= c`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call.

The constraints produced by the following two examples are identical.

**Swift**

```swift
// Creating a constraint using NSLayoutConstraint
NSLayoutConstraint(item: button,
                   attribute: .Width,
                   relatedBy: .GreaterThanOrEqual,
                   toItem: nil,
                   attribute: .NotAnAttribute,
                   multiplier: 1.0,
                   constant: 40.0).isActive = true
 
// Creating the same constraint using constraintGreaterThanOrEqualToConstant:
button.widthAnchor.constraintGreaterThanOrEqualToConstant(40.0).isActive = true
```

**Objective-C**

```objc
// Creating a constraint using NSLayoutConstraint
[NSLayoutConstraint
 constraintWithItem:self.button
 attribute:NSLayoutAttributeWidth
 relatedBy:NSLayoutRelationGreaterThanOrEqual
 toItem:nil
 attribute:NSLayoutAttributeNotAnAttribute
 multiplier:1.0
 constant:40.0].active = YES;
 
// Creating the same constraint using constraintGreaterThanOrEqualToConstant:
[self.button.widthAnchor constraintGreaterThanOrEqualToConstant: 40.0].active = YES;
```

## See Also

### Building constraints

- [- constraintEqualToAnchor:multiplier:](<constraint(equalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.
- [- constraintEqualToAnchor:multiplier:constant:](<constraint(equalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as equal to the specified size attribute multiplied by a constant plus an offset.
- [- constraintEqualToConstant:](<constraint(equaltoconstant_).md>) — Returns a constraint that defines a constant size for the anchor’s size attribute.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:](<constraint(greaterthanorequalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant.
- [- constraintGreaterThanOrEqualToAnchor:multiplier:constant:](<constraint(greaterthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintLessThanOrEqualToAnchor:multiplier:](<constraint(lessthanorequalto_multiplier_).md>) — Returns a constraint that defines the anchor’s size attribute as less than or equal to the specified anchor multiplied by the constant.
- [- constraintLessThanOrEqualToAnchor:multiplier:constant:](<constraint(lessthanorequalto_multiplier_constant_).md>) — Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [- constraintLessThanOrEqualToConstant:](<constraint(lessthanorequaltoconstant_).md>) — Returns a constraint that defines the maximum size for the anchor’s size attribute.
