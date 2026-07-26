---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textfieldstyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/textfieldstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfieldstyle/automatic.json'
content_hash: 'sha256:abc673d7125ab3b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextFieldStyle](../textfieldstyle.md)

# automatic

<sub>Type Property</sub>

The default text field style, based on the text field’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var automatic: DefaultTextFieldStyle { get }
```

## Discussion

The default style represents the recommended style based on the current platform and the text field’s context within the view hierarchy.

## See Also

### Getting built-in text field styles

- [bordered](bordered.md) — A text field style with a system-defined border whose shape is determined by the [textInputBorderShape(_:)](<../view/textinputbordershape(__).md>) modifier. _(beta)_
- [plain](plain.md) — A text field style with no decoration.
- [roundedBorder](roundedborder.md) — A text field style with a system-defined rounded border. _(deprecated)_
- [squareBorder](squareborder.md) — A text field style with a system-defined square border. _(deprecated)_
