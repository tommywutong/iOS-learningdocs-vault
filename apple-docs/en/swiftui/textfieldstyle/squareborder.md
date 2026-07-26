---
title: squareBorder
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/textfieldstyle/squareborder
source_url: 'https://developer.apple.com/documentation/swiftui/textfieldstyle/squareborder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfieldstyle/squareborder.json'
content_hash: 'sha256:669b1d7bca1f1a0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextFieldStyle](../textfieldstyle.md)

# squareBorder

<sub>Type Property</sub>

A text field style with a system-defined square border.

> [!warning] Deprecated
> Use `textFieldStyle(.bordered)` instead. As of macOS 26, text fields no longer have a rectangular border.

<sub>macOS</sub>

```swift
@export(implementation) static var squareBorder: SquareBorderTextFieldStyle { get }
```

## Discussion

As of macOS 26, text fields no longer have a rectangular border.

## See Also

### Getting built-in text field styles

- [automatic](automatic.md) — The default text field style, based on the text field’s context.
- [bordered](bordered.md) — A text field style with a system-defined border whose shape is determined by the [textInputBorderShape(_:)](<../view/textinputbordershape(__).md>) modifier. _(beta)_
- [plain](plain.md) — A text field style with no decoration.
- [roundedBorder](roundedborder.md) — A text field style with a system-defined rounded border. _(deprecated)_
