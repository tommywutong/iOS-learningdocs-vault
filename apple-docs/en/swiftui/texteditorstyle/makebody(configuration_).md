---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/texteditorstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/texteditorstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/texteditorstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:cea4bfdedcb1540e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextEditorStyle](../texteditorstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a text editor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the text editor.

## Discussion

The system calls this method for each [TextEditor](../texteditor.md) instance in a view hierarchy where this style is the current text editor style.

## See Also

### Creating custom styles

- [Configuration](configuration.md) — The properties of a text editor.
- [Body](body.md) — A view that represents the body of a text editor.
