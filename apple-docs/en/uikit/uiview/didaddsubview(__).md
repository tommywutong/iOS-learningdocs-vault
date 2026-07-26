---
title: 'didAddSubview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/didaddsubview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/didaddsubview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/didaddsubview%28_%3A%29.json'
content_hash: 'sha256:40fc53327883f4ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# didAddSubview(_:)

<sub>Instance Method</sub>

Tells the view that a subview was added.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didAddSubview(_ subview: UIView)
```

## Parameters

- `subview` — The view that was added as a subview.

## Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions when subviews are added. This method is called in response to adding a subview using any of the relevant view methods.

## See Also

### Related Documentation

- [- insertSubview:belowSubview:](<insertsubview(__belowsubview_).md>) — Inserts a view below another view in the view hierarchy.
- [- insertSubview:aboveSubview:](<insertsubview(__abovesubview_).md>) — Inserts a view above another view in the view hierarchy.
- [- addSubview:](<addsubview(__).md>) — Adds a view to the end of the receiver’s list of subviews.
- [- insertSubview:atIndex:](<insertsubview(__at_).md>) — Inserts a subview at the specified index.

### Observing view-related changes

- [- willRemoveSubview:](<willremovesubview(__).md>) — Tells the view that a subview is about to be removed.
- [- willMoveToSuperview:](<willmove(tosuperview_).md>) — Tells the view that its superview is about to change to the specified superview.
- [- didMoveToSuperview](<didmovetosuperview().md>) — Tells the view that its superview changed.
- [- willMoveToWindow:](<willmove(towindow_).md>) — Tells the view that its window object is about to change.
- [- didMoveToWindow](<didmovetowindow().md>) — Tells the view that its window object changed.
