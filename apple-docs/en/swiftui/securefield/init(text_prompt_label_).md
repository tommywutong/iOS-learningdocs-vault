---
title: 'init(text:prompt:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/securefield/init(text:prompt:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/securefield/init(text:prompt:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/securefield/init%28text%3Aprompt%3Alabel%3A%29.json'
content_hash: 'sha256:6b408eaa1915456e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SecureField](../securefield.md)

# init(text:prompt:label:)

<sub>Initializer</sub>

Creates a secure field with a prompt generated from a `Text`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(text: Binding<String>, prompt: Text? = nil, @ContentBuilder label: () -> Label)
```

## Parameters

- `text` — A binding to the text that the field displays and edits.

- `prompt` — A [Text](../text.md) view that represents the secure field’s prompt. The prompt provides guidance on what people should type into the secure field.

- `label` — A view that describes the purpose of the secure field.

## Discussion

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever someone submits this secure field — for example, by pressing the Return key.

## See Also

### Creating a secure text field

- [init(_:text:)](<init(__text_).md>) — Creates a secure field with a prompt generated from a `Text`.
- [init(_:text:prompt:)](<init(__text_prompt_).md>) — Creates a secure field with a prompt generated from a `Text`.
