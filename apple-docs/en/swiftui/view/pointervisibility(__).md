---
title: 'pointerVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/pointervisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/pointervisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/pointervisibility%28_%3A%29.json'
content_hash: 'sha256:4255e324804f65a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# pointerVisibility(_:)

<sub>Instance Method</sub>

Sets the visibility of the pointer when it’s over the view.

<sub>macOS</sub>

```swift
nonisolated func pointerVisibility(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — The pointer visibility to apply.

## Return Value

A view that changes the visibility of the pointer when hovered.

## See Also

### Modifying pointer appearance

- [pointerStyle(_:)](<pointerstyle(__).md>) — Sets the pointer style to display when the pointer is over the view.
- [PointerStyle](../pointerstyle.md) — A style describing the appearance of the pointer (also called a cursor) when it’s hovered over a view.
