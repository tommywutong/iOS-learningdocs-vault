---
title: 'onDisappear(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/ondisappear(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ondisappear(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ondisappear%28perform%3A%29.json'
content_hash: 'sha256:c576e59b110bf837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onDisappear(perform:)

<sub>Instance Method</sub>

Adds an action to perform after this view disappears.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onDisappear(perform action: (() -> Void)? = nil) -> some View

```

## Parameters

- `action` — The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A view that triggers `action` after it disappears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific view type that you apply it to, but the `action` closure doesn’t execute until the view disappears from the interface.

## See Also

### Responding to view life cycle updates

- [onAppear(perform:)](<onappear(perform_).md>) — Adds an action to perform before this view appears.
