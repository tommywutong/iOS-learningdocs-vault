---
title: TextFieldStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textfieldstyle
source_url: 'https://developer.apple.com/documentation/swiftui/textfieldstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfieldstyle.json'
content_hash: 'sha256:12a680fa4531f2a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextFieldStyle

<sub>Protocol</sub>

A specification for the appearance and interaction of a text field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TextFieldStyle
```

## Relationships

- **Conforming Types**: [BorderedTextFieldStyle](borderedtextfieldstyle.md), [DefaultTextFieldStyle](defaulttextfieldstyle.md), [PlainTextFieldStyle](plaintextfieldstyle.md), [RoundedBorderTextFieldStyle](roundedbordertextfieldstyle.md), [SquareBorderTextFieldStyle](squarebordertextfieldstyle.md)

## Topics

### Getting built-in text field styles

- [automatic](textfieldstyle/automatic.md) — The default text field style, based on the text field’s context.
- [bordered](textfieldstyle/bordered.md) — A text field style with a system-defined border whose shape is determined by the [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) modifier. _(beta)_
- [plain](textfieldstyle/plain.md) — A text field style with no decoration.
- [roundedBorder](textfieldstyle/roundedborder.md) — A text field style with a system-defined rounded border. _(deprecated)_
- [squareBorder](textfieldstyle/squareborder.md) — A text field style with a system-defined square border. _(deprecated)_

### Supporting types

- [BorderedTextFieldStyle](borderedtextfieldstyle.md) — A text field style with a system-defined border. _(beta)_
- [DefaultTextFieldStyle](defaulttextfieldstyle.md) — The default text field style, based on the text field’s context.
- [PlainTextFieldStyle](plaintextfieldstyle.md) — A text field style with no decoration.
- [RoundedBorderTextFieldStyle](roundedbordertextfieldstyle.md) — A text field style with a system-defined rounded border. _(deprecated)_
- [SquareBorderTextFieldStyle](squarebordertextfieldstyle.md) — A text field style with a system-defined square border. _(deprecated)_

## See Also

### Styling views that display text

- [labelStyle(_:)](<view/labelstyle(__).md>) — Sets the style for labels within this view.
- [LabelStyle](labelstyle.md) — A type that applies a custom appearance to all labels within a view.
- [LabelStyleConfiguration](labelstyleconfiguration.md) — The properties of a label.
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — Sets the style for text fields within this view.
- [textEditorStyle(_:)](<view/texteditorstyle(__).md>) — Sets the style for text editors within this view.
- [TextEditorStyle](texteditorstyle.md) — A specification for the appearance and interaction of a text editor.
- [TextEditorStyleConfiguration](texteditorstyleconfiguration.md) — The properties of a text editor.
