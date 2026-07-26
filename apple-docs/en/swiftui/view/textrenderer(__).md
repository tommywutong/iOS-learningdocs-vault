---
title: 'textRenderer(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/textrenderer(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textrenderer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textrenderer%28_%3A%29.json'
content_hash: 'sha256:85a7cf196cf4988e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textRenderer(_:)

<sub>Instance Method</sub>

Returns a new view such that any text views within it will use `renderer` to draw themselves.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func textRenderer<T>(_ renderer: T) -> some View where T : TextRenderer

```

## Parameters

- `renderer` — The renderer value.

## Return Value

A new view that will use `renderer` to draw its text views.

## See Also

### Rendering text

- [Creating visual effects with SwiftUI](../creating-visual-effects-with-swiftui.md) — Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [TextAttribute](../textattribute.md) — A value that you can attach to text views and that text renderers can query.
- [TextRenderer](../textrenderer.md) — A value that can replace the default text view rendering behavior.
- [TextProxy](../textproxy.md) — A proxy for a text view that custom text renderers use.
