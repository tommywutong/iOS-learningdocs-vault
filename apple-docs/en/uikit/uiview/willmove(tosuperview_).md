---
title: 'willMove(toSuperview:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/willmove(tosuperview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/willmove(tosuperview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/willmove%28tosuperview%3A%29.json'
content_hash: 'sha256:9a82795f92a3983d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# willMove(toSuperview:)

<sub>Instance Method</sub>

Tells the view that its superview is about to change to the specified superview.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func willMove(toSuperview newSuperview: UIView?)
```

## Parameters

- `newSuperview` — A view object that will be the new superview of the receiver. This object may be `nil`.

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the superview changes.

## See Also

### Observing view-related changes

- [- didAddSubview:](<didaddsubview(__).md>) — Tells the view that a subview was added.
- [- willRemoveSubview:](<willremovesubview(__).md>) — Tells the view that a subview is about to be removed.
- [- didMoveToSuperview](<didmovetosuperview().md>) — Tells the view that its superview changed.
- [- willMoveToWindow:](<willmove(towindow_).md>) — Tells the view that its window object is about to change.
- [- didMoveToWindow](<didmovetowindow().md>) — Tells the view that its window object changed.
