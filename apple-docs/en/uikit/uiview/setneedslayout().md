---
title: setNeedsLayout()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/setneedslayout()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setneedslayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setneedslayout%28%29.json'
content_hash: 'sha256:f3d7158bef12677c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setNeedsLayout()

<sub>Instance Method</sub>

Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsLayout()
```

## Discussion

Call this method on your application’s main thread when you want to adjust the layout of a view’s subviews. This method makes a note of the request and returns immediately. Because this method does not force an immediate update, but instead waits for the next update cycle, you can use it to invalidate the layout of multiple views before any of those views are updated. This behavior allows you to consolidate all of your layout updates to one update cycle, which is usually better for performance.

## See Also

### Laying out subviews

- [- layoutSubviews](<layoutsubviews().md>) — Lays out subviews.
- [- layoutIfNeeded](<layoutifneeded().md>) — Lays out the subviews immediately, if layout updates are pending.
- [requiresConstraintBasedLayout](requiresconstraintbasedlayout.md) — A Boolean value that indicates whether the receiver depends on the constraint-based layout system.
- [translatesAutoresizingMaskIntoConstraints](translatesautoresizingmaskintoconstraints.md) — A Boolean value that determines whether the view’s autoresizing mask converts to Auto Layout constraints.
