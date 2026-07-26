---
title: roundedBorder
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/textfieldstyle/roundedborder
source_url: 'https://developer.apple.com/documentation/swiftui/textfieldstyle/roundedborder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfieldstyle/roundedborder.json'
content_hash: 'sha256:bee08e65f58bc641'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextFieldStyle](../textfieldstyle.md)

# roundedBorder

<sub>Type Property</sub>

A text field style with a system-defined rounded border.

> [!warning] Deprecated
> Use `textFieldStyle(.bordered)` with `textInputBorderShape(.roundedRectangle)`

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static var roundedBorder: RoundedBorderTextFieldStyle { get }
```

## Discussion

Use [textFieldStyle(_:)](<../view/textfieldstyle(__).md>) to apply the [bordered](bordered.md) style with [textInputBorderShape(_:)](<../view/textinputbordershape(__).md>) to apply the [roundedRectangle](../textinputbordershape/roundedrectangle.md) shape instead.

## See Also

### Getting built-in text field styles

- [automatic](automatic.md) — The default text field style, based on the text field’s context.
- [bordered](bordered.md) — A text field style with a system-defined border whose shape is determined by the [textInputBorderShape(_:)](<../view/textinputbordershape(__).md>) modifier. _(beta)_
- [plain](plain.md) — A text field style with no decoration.
- [squareBorder](squareborder.md) — A text field style with a system-defined square border. _(deprecated)_
