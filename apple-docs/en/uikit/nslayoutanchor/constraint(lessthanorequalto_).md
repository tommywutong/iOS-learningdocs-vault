---
title: 'constraint(lessThanOrEqualTo:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutanchor/constraint(lessthanorequalto:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutanchor/constraint(lessthanorequalto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutanchor/constraint%28lessthanorequalto%3A%29.json'
content_hash: 'sha256:7db50ad3183c7f94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutAnchor](../nslayoutanchor.md)

# constraint(lessThanOrEqualTo:)

<sub>Instance Method</sub>

Returns a constraint that defines one item’s attribute as less than or equal to another.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraint(lessThanOrEqualTo anchor: NSLayoutAnchor<AnchorType>) -> NSLayoutConstraint
```

## Parameters

- `anchor` — A layout anchor from a [UIView](../uiview.md), [NSView](../../appkit/nsview.md), or [UILayoutGuide](../uilayoutguide.md) object. You must use a subclass of [NSLayoutAnchor](../nslayoutanchor.md) that matches the current anchor. For example, if you call this method on an [NSLayoutXAxisAnchor](../nslayoutxaxisanchor.md) object, this parameter must be another [NSLayoutXAxisAnchor](../nslayoutxaxisanchor.md).

## Return Value

An [NSLayoutConstraint](../nslayoutconstraint.md) object that defines the attribute represented by this layout anchor as less than or equal to the attribute represented by the `anchor` parameter.

## Discussion

This method defines the relationship `first attribute <= second attribute`. Where `first attribute` is the layout attribute represented by the anchor receiving this method call, and `second attribute` is the layout attribute represented by the `anchor` parameter. All values are measured in points; however, these values can be interpreted in different ways, depending on the type of layout anchor.

- For leading or trailing anchors, the values increase as you move in the current language’s reading direction. For English, values increase as you move to the right.
- For left and right anchors, the values increase as you move to the right.
- For [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md) objects, the values increase as you move down.
- For [NSLayoutDimension](../nslayoutdimension.md) objects, the values increase as the items increase in size.

The constraints produced by the following two examples are identical.

**Swift**

```swift
// Creating a constraint using NSLayoutConstraint
NSLayoutConstraint(item: subview,
                   attribute: .Leading,
                   relatedBy: .LessThanOrEqual,
                   toItem: view,
                   attribute: .LeadingMargin,
                   multiplier: 1.0,
                   constant: 0.0).isActive = true
 
// Creating the same constraint using constraintLessThanOrEqualToAnchor:
let margins = view.layoutMarginsGuide
subview.leadingAnchor.constraintLessThanOrEqualToAnchor(margins.leadingAnchor).isActive = true
```

**Objective-C**

```objc
// Creating a constraint using NSLayoutConstraint
[NSLayoutConstraint
 constraintWithItem:subview
 attribute:NSLayoutAttributeLeading
 relatedBy:NSLayoutRelationLessThanOrEqual
 toItem:self.view
 attribute:NSLayoutAttributeLeadingMargin
 multiplier:1.0
 constant:0.0].active = YES;
 
// Creating the same constraint using constraintLessThanOrEqualToAnchor:
UILayoutGuide *margin = self.view.layoutMarginsGuide;
[subview.leadingAnchor constraintLessThanOrEqualToAnchor:margin.leadingAnchor].active = YES;
```

## See Also

### Building constraints

- [- constraintEqualToAnchor:](<constraint(equalto_).md>) — Returns a constraint that defines one item’s attribute as equal to another.
- [- constraintEqualToAnchor:constant:](<constraint(equalto_constant_).md>) — Returns a constraint that defines one item’s attribute as equal to another item’s attribute plus a constant offset.
- [- constraintGreaterThanOrEqualToAnchor:](<constraint(greaterthanorequalto_).md>) — Returns a constraint that defines one item’s attribute as greater than or equal to another.
- [- constraintGreaterThanOrEqualToAnchor:constant:](<constraint(greaterthanorequalto_constant_).md>) — Returns a constraint that defines one item’s attribute as greater than or equal to another item’s attribute plus a constant offset.
- [- constraintLessThanOrEqualToAnchor:constant:](<constraint(lessthanorequalto_constant_).md>) — Returns a constraint that defines one item’s attribute as less than or equal to another item’s attribute plus a constant offset.
