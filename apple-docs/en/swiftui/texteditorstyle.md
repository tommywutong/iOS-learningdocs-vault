---
title: TextEditorStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/texteditorstyle
source_url: 'https://developer.apple.com/documentation/swiftui/texteditorstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/texteditorstyle.json'
content_hash: 'sha256:d77e6a149cb7d44c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextEditorStyle

<sub>Protocol</sub>

A specification for the appearance and interaction of a text editor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol TextEditorStyle
```

## Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [AutomaticTextEditorStyle](automatictexteditorstyle.md), [PlainTextEditorStyle](plaintexteditorstyle.md), [RoundedBorderTextEditorStyle](roundedbordertexteditorstyle.md)

## Topics

### Getting built-in styles

- [automatic](texteditorstyle/automatic.md) — The default text editor style, based on the text editor’s context.
- [plain](texteditorstyle/plain.md) — A text editor style with no decoration.
- [roundedBorder](texteditorstyle/roundedborder.md) — A text editor style with a system-defined rounded border.

### Creating custom styles

- [makeBody(configuration:)](<texteditorstyle/makebody(configuration_).md>) — Creates a view that represents the body of a text editor.
- [Configuration](texteditorstyle/configuration.md) — The properties of a text editor.
- [Body](texteditorstyle/body.md) — A view that represents the body of a text editor.

### Supporting types

- [AutomaticTextEditorStyle](automatictexteditorstyle.md) — The default text editor style, based on the text editor’s context.
- [PlainTextEditorStyle](plaintexteditorstyle.md) — A text editor style with no decoration.
- [RoundedBorderTextEditorStyle](roundedbordertexteditorstyle.md) — A text editor style with a system-defined rounded border.

## See Also

### Styling views that display text

- [labelStyle(_:)](<view/labelstyle(__).md>) — Sets the style for labels within this view.
- [LabelStyle](labelstyle.md) — A type that applies a custom appearance to all labels within a view.
- [LabelStyleConfiguration](labelstyleconfiguration.md) — The properties of a label.
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — Sets the style for text fields within this view.
- [TextFieldStyle](textfieldstyle.md) — A specification for the appearance and interaction of a text field.
- [textEditorStyle(_:)](<view/texteditorstyle(__).md>) — Sets the style for text editors within this view.
- [TextEditorStyleConfiguration](texteditorstyleconfiguration.md) — The properties of a text editor.
