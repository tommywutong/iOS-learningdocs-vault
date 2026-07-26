---
title: translatesAutoresizingMaskIntoConstraints
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/translatesautoresizingmaskintoconstraints
source_url: 'https://developer.apple.com/documentation/uikit/uiview/translatesautoresizingmaskintoconstraints'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/translatesautoresizingmaskintoconstraints.json'
content_hash: 'sha256:4f81c4a87f929124'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# translatesAutoresizingMaskIntoConstraints

<sub>Instance Property</sub>

A Boolean value that determines whether the view’s autoresizing mask converts to Auto Layout constraints.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var translatesAutoresizingMaskIntoConstraints: Bool { get set }
```

## Discussion

If this property’s value is [true](../../swift/true.md), the system creates a set of constraints that duplicate the behavior specified by the view’s autoresizing mask. You can also modify the view’s size and location using the view’s [frame](frame.md), [bounds](bounds.md), or [center](center.md) properties, creating a static, frame-based layout within Auto Layout.

Because the autoresizing mask constraints specify the view’s size and position, you can’t add constraints to modify this size or position without introducing conflicts. To use Auto Layout to dynamically calculate the size and position of your view, set this property to [false](../../swift/false.md), and then provide a nonambiguous, nonconflicting set of constraints for the view.

Set this property on a subview from a containing superview or view controller, not from within the view itself:

```swift
customSubview.translatesAutoresizingMaskIntoConstraints = false
```

Don’t set this property on `self` inside a custom view’s own code, because this prevents the containing superview from managing its layout. Don’t modify this property’s value for views that UIKit classes manage, such as [UITableViewCell](../uitableviewcell.md), [arrangedSubviews](../uistackview/arrangedsubviews.md), and [view](../uiviewcontroller/view.md). These classes handle layout automatically, and changing this property interferes with their layout behavior.

By default, the system sets this property to [true](../../swift/true.md) for any view you programmatically create. If you add views in Interface Builder, the system automatically sets this property to [false](../../swift/false.md).

## See Also

### Laying out subviews

- [- layoutSubviews](<layoutsubviews().md>) — Lays out subviews.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [- layoutIfNeeded](<layoutifneeded().md>) — Lays out the subviews immediately, if layout updates are pending.
- [requiresConstraintBasedLayout](requiresconstraintbasedlayout.md) — A Boolean value that indicates whether the receiver depends on the constraint-based layout system.
