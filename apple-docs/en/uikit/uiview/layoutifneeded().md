---
title: layoutIfNeeded()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/layoutifneeded()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/layoutifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/layoutifneeded%28%29.json'
content_hash: 'sha256:cc44cc619cbcf579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# layoutIfNeeded()

<sub>Instance Method</sub>

Lays out the subviews immediately, if layout updates are pending.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutIfNeeded()
```

## Discussion

Use this method to force the view to update its layout immediately. When using Auto Layout, the layout engine updates the position of views as needed to satisfy changes in constraints. Using the view that receives the message as the root view, this method lays out the view subtree starting at the root.  If no layout updates are pending, this method exits without modifying the layout or calling any layout-related callbacks.

## See Also

### Laying out subviews

- [- layoutSubviews](<layoutsubviews().md>) — Lays out subviews.
- [- setNeedsLayout](<setneedslayout().md>) — Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [requiresConstraintBasedLayout](requiresconstraintbasedlayout.md) — A Boolean value that indicates whether the receiver depends on the constraint-based layout system.
- [translatesAutoresizingMaskIntoConstraints](translatesautoresizingmaskintoconstraints.md) — A Boolean value that determines whether the view’s autoresizing mask converts to Auto Layout constraints.
