---
title: 'insertArrangedSubview(_:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistackview/insertarrangedsubview(_:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/insertarrangedsubview(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/insertarrangedsubview%28_%3Aat%3A%29.json'
content_hash: 'sha256:e895b65e1523d53b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# insertArrangedSubview(_:at:)

<sub>Instance Method</sub>

Adds the provided view to the array of arranged subviews at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertArrangedSubview(_ view: UIView, at stackIndex: Int)
```

## Parameters

- `view` — The view to add to the array of views arranged by the stack.

- `stackIndex` — The index where the stack inserts the new view in its [arrangedSubviews](arrangedsubviews.md) array. This value must not be greater than the number of views currently in this array. If the index is out of bounds, this method throws an [internalInconsistencyException](../../foundation/nsexceptionname/internalinconsistencyexception.md) exception.

## Discussion

If index is already occupied, the stack view increases the size of the [arrangedSubviews](arrangedsubviews.md) array and shifts all of its contents at the index and above to the next higher space in the array. Then the stack view stores the provided view at the index.

The stack view also ensures that the [arrangedSubviews](arrangedsubviews.md) array is always a subset of its [subviews](../uiview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it isn’t already. When adding subviews, the stack view appends the view to the end of its [subviews](../uiview/subviews.md) array. The index only affects the order of views in the [arrangedSubviews](arrangedsubviews.md) array. It doesn’t affect the ordering of views in the [subviews](../uiview/subviews.md) array.

## See Also

### Related Documentation

- [- removeFromSuperview](<../uiview/removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- initWithArrangedSubviews:](<init(arrangedsubviews_).md>) — Returns a new stack view object that manages the provided views.

### Managing arranged subviews

- [- addArrangedSubview:](<addarrangedsubview(__).md>) — Adds a view to the end of the arranged subviews array.
- [arrangedSubviews](arrangedsubviews.md) — The list of views arranged by the stack view.
- [- removeArrangedSubview:](<removearrangedsubview(__).md>) — Removes the provided view from the stack’s array of arranged subviews.
