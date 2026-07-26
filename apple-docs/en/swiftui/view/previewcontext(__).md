---
title: 'previewContext(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/previewcontext(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/previewcontext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/previewcontext%28_%3A%29.json'
content_hash: 'sha256:8b94f980e67ca84b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# previewContext(_:)

<sub>Instance Method</sub>

Declares a context for the preview.

> [!warning] Deprecated
> Use [Preview(_:body:)](<../preview(__body_).md>) with a WidgetKit timeline provider or entries instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func previewContext<C>(_ value: C) -> some View where C : PreviewContext

```

## Parameters

- `value` — The context for the preview; the default is `nil`.

## See Also

### Setting a context

- [PreviewContext](../previewcontext.md) — A context type for use with a preview. _(deprecated)_
- [PreviewContextKey](../previewcontextkey.md) — A key type for a preview context. _(deprecated)_
