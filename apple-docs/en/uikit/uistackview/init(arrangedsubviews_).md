---
title: 'init(arrangedSubviews:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistackview/init(arrangedsubviews:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistackview/init(arrangedsubviews:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistackview/init%28arrangedsubviews%3A%29.json'
content_hash: 'sha256:0b6459d9f381b2e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStackView](../uistackview.md)

# init(arrangedSubviews:)

<sub>Initializer</sub>

Returns a new stack view object that manages the provided views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(arrangedSubviews views: [UIView])
```

## Parameters

- `views` — The views to be arranged by the stack view.

## Return Value

A new stack view object. This stack view contains and lays out the provided views in a single stack. You can modify the orientation or appearance of this stack, using the stack view’s properties.

## Discussion

The stack view adds all the arranged views to its [arrangedSubviews](arrangedsubviews.md) array. It also adds these views as subviews. If any view contained in the `arrangedSubviews` array receives a [- removeFromSuperview](<../uiview/removefromsuperview().md>) method call, the stack view also removes it from the `arrangedSubviews`.

## See Also

### Related Documentation

- [- insertArrangedSubview:atIndex:](<insertarrangedsubview(__at_).md>) — Adds the provided view to the array of arranged subviews at the specified index.
- [- removeFromSuperview](<../uiview/removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [arrangedSubviews](arrangedsubviews.md) — The list of views arranged by the stack view.
- [- addArrangedSubview:](<addarrangedsubview(__).md>) — Adds a view to the end of the arranged subviews array.
- [- removeArrangedSubview:](<removearrangedsubview(__).md>) — Removes the provided view from the stack’s array of arranged subviews.

### Initializing a stack view

- [- initWithFrame:](<init(frame_).md>) — Creates a stack view with the specified frame.
- [- initWithCoder:](<init(coder_).md>) — Creates a stack view from data in an unarchiver.
