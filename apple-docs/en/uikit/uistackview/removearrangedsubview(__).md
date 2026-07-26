---
title: 'removeArrangedSubview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistackview/removearrangedsubview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/removearrangedsubview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/removearrangedsubview%28_%3A%29.json'
content_hash: 'sha256:e725dd0d55a39505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# removeArrangedSubview(_:)

<sub>Instance Method</sub>

Removes the provided view from the stack’s array of arranged subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeArrangedSubview(_ view: UIView)
```

## Parameters

- `view` — The view to be removed from the array of views arranged by the stack.

## Discussion

This method removes the provided view from the stack’s [arrangedSubviews](arrangedsubviews.md) array. The stack view no longer manages the view’s position and size. However, this method doesn’t remove the provided view from the stack’s [subviews](../uiview/subviews.md) array; therefore, the view is still displayed as part of the view hierarchy.

To prevent the view from appearing on screen after calling the stack’s [- removeArrangedSubview:](<removearrangedsubview(__).md>) method, explicitly remove the view from the subviews array by calling the view’s [- removeFromSuperview](<../uiview/removefromsuperview().md>) method, or set the view’s [hidden](../uiview/ishidden.md) property to [true](../../swift/true.md).

## See Also

### Related Documentation

- [- removeFromSuperview](<../uiview/removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- initWithArrangedSubviews:](<init(arrangedsubviews_).md>) — Returns a new stack view object that manages the provided views.

### Managing arranged subviews

- [- addArrangedSubview:](<addarrangedsubview(__).md>) — Adds a view to the end of the arranged subviews array.
- [arrangedSubviews](arrangedsubviews.md) — The list of views arranged by the stack view.
- [- insertArrangedSubview:atIndex:](<insertarrangedsubview(__at_).md>) — Adds the provided view to the array of arranged subviews at the specified index.
