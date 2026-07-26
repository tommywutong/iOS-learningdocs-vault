---
title: 'focusable(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/focusable(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/focusable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/focusable%28_%3A%29.json'
content_hash: 'sha256:619b37ef506825f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# focusable(_:)

<sub>Instance Method</sub>

Specifies if the view is focusable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func focusable(_ isFocusable: Bool = true) -> some View

```

## Parameters

- `isFocusable` — A Boolean value that indicates whether this view is focusable.

## Return Value

A view that sets whether a view is focusable.

## See Also

### Indicating that a view can receive focus

- [focusable(_:interactions:)](<focusable(__interactions_).md>) — Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [FocusInteractions](../focusinteractions.md) — Values describe different focus interactions that a view can support.
