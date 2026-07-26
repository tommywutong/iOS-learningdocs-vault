---
title: 'init(_:prompt:onSubmit:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textfieldlink/init(_:prompt:onsubmit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfieldlink/init(_:prompt:onsubmit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfieldlink/init%28_%3Aprompt%3Aonsubmit%3A%29.json'
content_hash: 'sha256:cdc7bcd162710da2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextFieldLink](../textfieldlink.md)

# init(_:prompt:onSubmit:)

<sub>Initializer</sub>

Creates a TextFieldLink which when pressed will request text input from the user.

<sub>watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, prompt: Text? = nil, onSubmit: @escaping (String) -> Void)
```

## Parameters

- `titleResource` — A key for the TextFieldLink’s localized title, that describes the purpose of requesting text input.

- `prompt` — Text which describes the reason for requesting text input.

- `onSubmit` — An action to perform when text input has been accepted and dismissed.

## See Also

### Creating a text field link

- [init(prompt:label:onSubmit:)](<init(prompt_label_onsubmit_).md>) — Creates a TextFieldLink which when pressed will request text input from the user.
