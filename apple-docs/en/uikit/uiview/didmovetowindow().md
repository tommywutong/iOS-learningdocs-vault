---
title: didMoveToWindow()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/didmovetowindow()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/didmovetowindow()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/didmovetowindow%28%29.json'
content_hash: 'sha256:0e06b4ba952d0c48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# didMoveToWindow()

<sub>Instance Method</sub>

Tells the view that its window object changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didMoveToWindow()
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the window changes.

The [window](window.md) property may be `nil` by the time that this method is called, indicating that the receiver does not currently reside in any window. This occurs when the receiver has just been removed from its superview or when the receiver has just been added to a superview that is not attached to a window. Overrides of this method may choose to ignore such cases if they are not of interest.

## See Also

### Observing view-related changes

- [- didAddSubview:](<didaddsubview(__).md>) — Tells the view that a subview was added.
- [- willRemoveSubview:](<willremovesubview(__).md>) — Tells the view that a subview is about to be removed.
- [- willMoveToSuperview:](<willmove(tosuperview_).md>) — Tells the view that its superview is about to change to the specified superview.
- [- didMoveToSuperview](<didmovetosuperview().md>) — Tells the view that its superview changed.
- [- willMoveToWindow:](<willmove(towindow_).md>) — Tells the view that its window object is about to change.
