---
title: 'addArrangedSubview(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistackview/addarrangedsubview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/addarrangedsubview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/addarrangedsubview%28_%3A%29.json'
content_hash: 'sha256:0a05da57d37f849b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# addArrangedSubview(_:)

<sub>Instance Method</sub>

Adds a view to the end of the arranged subviews array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addArrangedSubview(_ view: UIView)
```

## Parameters

- `view` — The view to add to the array of views arranged by the stack.

## Discussion

The stack view ensures that the [arrangedSubviews](arrangedsubviews.md) array is always a subset of its [subviews](../uiview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it isn’t already. If the view is already a subview, this operation doesn’t alter the subview ordering.

## See Also

### Related Documentation

- [- removeFromSuperview](<../uiview/removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- initWithArrangedSubviews:](<init(arrangedsubviews_).md>) — Returns a new stack view object that manages the provided views.

### Managing arranged subviews

- [arrangedSubviews](arrangedsubviews.md) — The list of views arranged by the stack view.
- [- insertArrangedSubview:atIndex:](<insertarrangedsubview(__at_).md>) — Adds the provided view to the array of arranged subviews at the specified index.
- [- removeArrangedSubview:](<removearrangedsubview(__).md>) — Removes the provided view from the stack’s array of arranged subviews.
