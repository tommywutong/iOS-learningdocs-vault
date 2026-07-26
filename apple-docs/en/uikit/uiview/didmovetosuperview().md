---
title: didMoveToSuperview()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/didmovetosuperview()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/didmovetosuperview()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/didmovetosuperview%28%29.json'
content_hash: 'sha256:d195978f9e274250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# didMoveToSuperview()

<sub>Instance Method</sub>

Tells the view that its superview changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didMoveToSuperview()
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the superview changes.

## See Also

### Observing view-related changes

- [- didAddSubview:](<didaddsubview(__).md>) — Tells the view that a subview was added.
- [- willRemoveSubview:](<willremovesubview(__).md>) — Tells the view that a subview is about to be removed.
- [- willMoveToSuperview:](<willmove(tosuperview_).md>) — Tells the view that its superview is about to change to the specified superview.
- [- willMoveToWindow:](<willmove(towindow_).md>) — Tells the view that its window object is about to change.
- [- didMoveToWindow](<didmovetowindow().md>) — Tells the view that its window object changed.
