---
title: arrangedSubviews
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistackview/arrangedsubviews
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/arrangedsubviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/arrangedsubviews.json'
content_hash: 'sha256:f3c99f307e0f1841'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# arrangedSubviews

<sub>Instance Property</sub>

The list of views arranged by the stack view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var arrangedSubviews: [UIView] { get }
```

## Discussion

The stack view ensures that the [arrangedSubviews](arrangedsubviews.md) array is always a subset of its [subviews](../uiview/subviews.md) array. Therefore, whenever the [- addArrangedSubview:](<addarrangedsubview(__).md>) method is called, the stack view adds the view as a subview, if it isn’t already. Whenever an arranged view’s [- removeFromSuperview](<../uiview/removefromsuperview().md>) method is called, the stack view removes the view from its [arrangedSubviews](arrangedsubviews.md) array.

## See Also

### Related Documentation

- [- removeFromSuperview](<../uiview/removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- initWithArrangedSubviews:](<init(arrangedsubviews_).md>) — Returns a new stack view object that manages the provided views.

### Managing arranged subviews

- [- addArrangedSubview:](<addarrangedsubview(__).md>) — Adds a view to the end of the arranged subviews array.
- [- insertArrangedSubview:atIndex:](<insertarrangedsubview(__at_).md>) — Adds the provided view to the array of arranged subviews at the specified index.
- [- removeArrangedSubview:](<removearrangedsubview(__).md>) — Removes the provided view from the stack’s array of arranged subviews.
