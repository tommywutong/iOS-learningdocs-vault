---
title: TextFieldLink
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textfieldlink
source_url: 'https://developer.apple.com/documentation/swiftui/textfieldlink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfieldlink.json'
content_hash: 'sha256:e075074adeba44ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextFieldLink

<sub>Structure</sub>

A control that requests text input from the user when pressed.

<sub>watchOS</sub>

```swift
nonisolated struct TextFieldLink<Label> where Label : View
```

## Overview

A `TextFieldLink` should be used to request text input from the user through a button interface.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a text field link

- [init(_:prompt:onSubmit:)](<textfieldlink/init(__prompt_onsubmit_).md>) — Creates a TextFieldLink which when pressed will request text input from the user.
- [init(prompt:label:onSubmit:)](<textfieldlink/init(prompt_label_onsubmit_).md>) — Creates a TextFieldLink which when pressed will request text input from the user.

## See Also

### Linking to other content

- [Link](link.md) — A control for navigating to a URL.
- [ShareLink](sharelink.md) — A view that controls a sharing presentation.
- [SharePreview](sharepreview.md) — A representation of a type to display in a share preview.
- [HelpLink](helplink.md) — A button with a standard appearance that opens app-specific help documentation.
