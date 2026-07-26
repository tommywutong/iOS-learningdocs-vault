---
title: 'willRemoveSubview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/willremovesubview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/willremovesubview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/willremovesubview%28_%3A%29.json'
content_hash: 'sha256:04dd054f3b33401c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# willRemoveSubview(_:)

<sub>Instance Method</sub>

Tells the view that a subview is about to be removed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func willRemoveSubview(_ subview: UIView)
```

## Parameters

- `subview` — The subview that will be removed.

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever subviews are removed. This method is called when the subview’s superview changes or when the subview is removed from the view hierarchy completely.

## See Also

### Related Documentation

- [- removeFromSuperview](<removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.

### Observing view-related changes

- [- didAddSubview:](<didaddsubview(__).md>) — Tells the view that a subview was added.
- [- willMoveToSuperview:](<willmove(tosuperview_).md>) — Tells the view that its superview is about to change to the specified superview.
- [- didMoveToSuperview](<didmovetosuperview().md>) — Tells the view that its superview changed.
- [- willMoveToWindow:](<willmove(towindow_).md>) — Tells the view that its window object is about to change.
- [- didMoveToWindow](<didmovetowindow().md>) — Tells the view that its window object changed.
