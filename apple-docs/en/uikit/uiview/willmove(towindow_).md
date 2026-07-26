---
title: 'willMove(toWindow:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/willmove(towindow:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/willmove(towindow:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/willmove%28towindow%3A%29.json'
content_hash: 'sha256:2dd157a5bc2da2c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# willMove(toWindow:)

<sub>Instance Method</sub>

Tells the view that its window object is about to change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func willMove(toWindow newWindow: UIWindow?)
```

## Parameters

- `newWindow` — The window object that will be at the root of the receiver’s new view hierarchy. This parameter may be `nil`.

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the window changes.

## See Also

### Observing view-related changes

- [- didAddSubview:](<didaddsubview(__).md>) — Tells the view that a subview was added.
- [- willRemoveSubview:](<willremovesubview(__).md>) — Tells the view that a subview is about to be removed.
- [- willMoveToSuperview:](<willmove(tosuperview_).md>) — Tells the view that its superview is about to change to the specified superview.
- [- didMoveToSuperview](<didmovetosuperview().md>) — Tells the view that its superview changed.
- [- didMoveToWindow](<didmovetowindow().md>) — Tells the view that its window object changed.
