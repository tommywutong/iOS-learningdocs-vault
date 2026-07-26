---
title: requiresConstraintBasedLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/requiresconstraintbasedlayout
source_url: 'https://developer.apple.com/documentation/uikit/uiview/requiresconstraintbasedlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/requiresconstraintbasedlayout.json'
content_hash: 'sha256:ecdebe469f1b72d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# requiresConstraintBasedLayout

<sub>Type Property</sub>

A Boolean value that indicates whether the receiver depends on the constraint-based layout system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var requiresConstraintBasedLayout: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the view must be in a window using constraint-based layout to function properly, [false](../../swift/false.md) otherwise.

## Discussion

Custom views should override this to return [true](../../swift/true.md) if they cannot layout correctly using autoresizing.

## See Also

### Laying out subviews

- [- layoutSubviews](<layoutsubviews().md>) — Lays out subviews.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [- layoutIfNeeded](<layoutifneeded().md>) — Lays out the subviews immediately, if layout updates are pending.
- [translatesAutoresizingMaskIntoConstraints](translatesautoresizingmaskintoconstraints.md) — A Boolean value that determines whether the view’s autoresizing mask converts to Auto Layout constraints.
