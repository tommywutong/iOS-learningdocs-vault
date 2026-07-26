---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/texteditorstyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/texteditorstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/texteditorstyle/automatic.json'
content_hash: 'sha256:1d6948e6093d3b64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextEditorStyle](../texteditorstyle.md)

# automatic

<sub>Type Property</sub>

The default text editor style, based on the text editor’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var automatic: AutomaticTextEditorStyle { get }
```

## Discussion

The default style represents the recommended style based on the current platform and the text editor’s context within the view hierarchy.

## See Also

### Getting built-in styles

- [plain](plain.md) — A text editor style with no decoration.
- [roundedBorder](roundedborder.md) — A text editor style with a system-defined rounded border.
