---
title: 'init(prompt:label:onSubmit:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textfieldlink/init(prompt:label:onsubmit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfieldlink/init(prompt:label:onsubmit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfieldlink/init%28prompt%3Alabel%3Aonsubmit%3A%29.json'
content_hash: 'sha256:6a5d36626ce07f62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextFieldLink](../textfieldlink.md)

# init(prompt:label:onSubmit:)

<sub>Initializer</sub>

Creates a TextFieldLink which when pressed will request text input from the user.

<sub>watchOS</sub>

```swift
nonisolated init(prompt: Text? = nil, @ContentBuilder label: () -> Label, onSubmit: @escaping (String) -> Void)
```

## Parameters

- `prompt` — Text which describes the reason for requesting text input.

- `label` — A view that describes the action of requesting text input.

- `onSubmit` — An action to perform when text input has been accepted and dismissed

## See Also

### Creating a text field link

- [init(_:prompt:onSubmit:)](<init(__prompt_onsubmit_).md>) — Creates a TextFieldLink which when pressed will request text input from the user.
