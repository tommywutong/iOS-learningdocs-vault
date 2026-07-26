---
title: BorderedTextFieldStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/borderedtextfieldstyle
source_url: 'https://developer.apple.com/documentation/swiftui/borderedtextfieldstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/borderedtextfieldstyle.json'
content_hash: 'sha256:e4635572f0605507'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BorderedTextFieldStyle

<sub>Structure</sub>

A text field style with a system-defined border.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BorderedTextFieldStyle
```

## Overview

The shape of the border is determined by the [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) modifier.

You can also use [bordered](textfieldstyle/bordered.md) to construct this style.

## Relationships

- **Conforms To**: [TextFieldStyle](textfieldstyle.md)

## Topics

### Initializers

- [init()](<borderedtextfieldstyle/init().md>) _(beta)_

## See Also

### Supporting types

- [DefaultTextFieldStyle](defaulttextfieldstyle.md) — The default text field style, based on the text field’s context.
- [PlainTextFieldStyle](plaintextfieldstyle.md) — A text field style with no decoration.
- [RoundedBorderTextFieldStyle](roundedbordertextfieldstyle.md) — A text field style with a system-defined rounded border. _(deprecated)_
- [SquareBorderTextFieldStyle](squarebordertextfieldstyle.md) — A text field style with a system-defined square border. _(deprecated)_
