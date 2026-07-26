---
title: NSLayoutAnchor
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutanchor
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutanchor.json'
content_hash: 'sha256:afffc7a0a6d71b3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSLayoutAnchor

<sub>Class</sub>

A factory class for creating layout constraint objects using a fluent API.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSLayoutAnchor<AnchorType> where AnchorType : AnyObject
```

## Overview

Use these constraints to programatically define your layout using Auto Layout. Instead of creating [NSLayoutConstraint](nslayoutconstraint.md) objects directly, start with a [UIView](uiview.md), [NSView](../appkit/nsview.md), or [UILayoutGuide](uilayoutguide.md) object you wish to constrain, and select one of that object’s anchor properties. These properties correspond to the main [Attribute](nslayoutconstraint/attribute.md) values used in Auto Layout, and provide an appropriate [NSLayoutAnchor](nslayoutanchor.md) subclass for creating constraints to that attribute. Use the anchor’s methods to construct your constraint.

> [!note] Note
> [UIView](uiview.md) does not provide anchor properties for the layout margin attributes. Instead, the [layoutMarginsGuide](uiview/layoutmarginsguide.md) property provides a [UILayoutGuide](uilayoutguide.md) object that represents these margins. Use the guide’s anchor properties to create your constraints.

**Swift**

```swift
// Creating constraints using NSLayoutConstraint
NSLayoutConstraint(item: subview,
                   attribute: .leading,
                   relatedBy: .equal,
                   toItem: view,
                   attribute: .leadingMargin,
                   multiplier: 1.0,
                   constant: 0.0).isActive = true

NSLayoutConstraint(item: subview,
                   attribute: .trailing,
                   relatedBy: .equal,
                   toItem: view,
                   attribute: .trailingMargin,
                   multiplier: 1.0,
                   constant: 0.0).isActive = true

// Creating the same constraints using Layout Anchors
let margins = view.layoutMarginsGuide

subview.leadingAnchor.constraint(equalTo: margins.leadingAnchor).isActive = true
subview.trailingAnchor.constraint(equalTo: margins.trailingAnchor).isActive = true

```

**Objective-C**

```objc
// Creating constraints using NSLayoutConstraint
[NSLayoutConstraint
 constraintWithItem:subview
 attribute:NSLayoutAttributeLeading
 relatedBy:NSLayoutRelationEqual
 toItem:self.view
 attribute:NSLayoutAttributeLeadingMargin
 multiplier:1.0
 constant:0.0].active = YES;
 
[NSLayoutConstraint
 constraintWithItem:subview
 attribute:NSLayoutAttributeTrailing
 relatedBy:NSLayoutRelationEqual
 toItem:self.view
 attribute:NSLayoutAttributeTrailingMargin
 multiplier:1.0
 constant:0.0].active = YES;
 
// Creating the same constraints using Layout Anchors
UILayoutGuide *margin = self.view.layoutMarginsGuide;
 
[subview.leadingAnchor constraintEqualToAnchor:margin.leadingAnchor].active = YES;
[subview.trailingAnchor constraintEqualToAnchor:margin.trailingAnchor].active = YES;
```

As you can see from these examples, the [NSLayoutAnchor](nslayoutanchor.md) class provides several advantages over using the [NSLayoutConstraint](nslayoutconstraint.md) API directly.

- The code is cleaner, more concise, and easier to read.
- The [Attribute](nslayoutconstraint/attribute.md) subclasses provide additional type checking, preventing you from creating invalid constraints.

> [!note] Note
> While the [NSLayoutAnchor](nslayoutanchor.md) class provides additional type checking, it is still possible to create invalid constraints. For example, the compiler allows you to constrain one view’s [leadingAnchor](uiview/leadinganchor.md) with another view’s [leftAnchor](uiview/leftanchor.md), since they are both [NSLayoutXAxisAnchor](nslayoutxaxisanchor.md) instances. However, Auto Layout does not allow constraints that mix leading and trailing attributes with left or right attributes. As a result, this constraint crashes at runtime.

For more information on the anchor properties, see [bottomAnchor](../appkit/nsview/bottomanchor.md) in the [UIView](uiview.md), [NSView](../appkit/nsview.md), or [UILayoutGuide](uilayoutguide.md).

> [!note] Note
> You never use the [NSLayoutAnchor](nslayoutanchor.md) class directly. Instead, use one of its subclasses, based on the type of constraint you wish to create.
>
> - Use [NSLayoutXAxisAnchor](nslayoutxaxisanchor.md) to create horizontal constraints.
> - Use [NSLayoutYAxisAnchor](nslayoutyaxisanchor.md) to create vertical constraints.
> - Use [NSLayoutDimension](nslayoutdimension.md) to create constraints that affect the view’s height or width.
>
> However, since you access [NSLayoutAnchor](nslayoutanchor.md) objects using the anchor properties of a [UIView](uiview.md), [NSView](../appkit/nsview.md), or [UILayoutGuide](uilayoutguide.md), a correct subclass is automatically provided.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSLayoutDimension](nslayoutdimension.md), [NSLayoutXAxisAnchor](nslayoutxaxisanchor.md), [NSLayoutYAxisAnchor](nslayoutyaxisanchor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Building constraints

- [- constraintEqualToAnchor:](<nslayoutanchor/constraint(equalto_).md>) — Returns a constraint that defines one item’s attribute as equal to another.
- [- constraintEqualToAnchor:constant:](<nslayoutanchor/constraint(equalto_constant_).md>) — Returns a constraint that defines one item’s attribute as equal to another item’s attribute plus a constant offset.
- [- constraintGreaterThanOrEqualToAnchor:](<nslayoutanchor/constraint(greaterthanorequalto_).md>) — Returns a constraint that defines one item’s attribute as greater than or equal to another.
- [- constraintGreaterThanOrEqualToAnchor:constant:](<nslayoutanchor/constraint(greaterthanorequalto_constant_).md>) — Returns a constraint that defines one item’s attribute as greater than or equal to another item’s attribute plus a constant offset.
- [- constraintLessThanOrEqualToAnchor:](<nslayoutanchor/constraint(lessthanorequalto_).md>) — Returns a constraint that defines one item’s attribute as less than or equal to another.
- [- constraintLessThanOrEqualToAnchor:constant:](<nslayoutanchor/constraint(lessthanorequalto_constant_).md>) — Returns a constraint that defines one item’s attribute as less than or equal to another item’s attribute plus a constant offset.

### Debugging the anchor

- [constraintsAffectingLayout](../appkit/nslayoutanchor/constraintsaffectinglayout.md) — The constraints that impact the layout of the anchor.
- [hasAmbiguousLayout](../appkit/nslayoutanchor/hasambiguouslayout.md) — A Boolean value indicating whether the constraints impacting the anchor specify its location ambiguously.
- [name](../appkit/nslayoutanchor/name.md) — The name assigned to the anchor for debugging purposes.
- [item](../appkit/nslayoutanchor/item.md) — The layout item used to calculate the anchor’s position.

### Initializers

- [init(coder:)](<nslayoutanchor/init(coder_).md>)

## See Also

### Anchors

- [NSLayoutXAxisAnchor](nslayoutxaxisanchor.md) — A factory class for creating horizontal layout constraint objects using a fluent API.
- [NSLayoutYAxisAnchor](nslayoutyaxisanchor.md) — A factory class for creating vertical layout constraint objects using a fluent API.
- [NSLAYOUTANCHOR_H](nslayoutanchor_h.md)
