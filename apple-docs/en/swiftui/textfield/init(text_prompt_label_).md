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
doc_path: '/documentation/swiftui/textfield/init(text:prompt:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(text:prompt:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28text%3Aprompt%3Alabel%3A%29.json'
content_hash: 'sha256:cb439ba8c4924b6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(text:prompt:label:)

<sub>Initializer</sub>

Creates a text field with a prompt generated from a `Text`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(text: Binding<String>, prompt: Text? = nil, @ContentBuilder label: () -> Label)
```

## Parameters

- `text` — The text to display and edit.

- `prompt` — A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.

- `label` — A view that describes the purpose of the text field.

## Discussion

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever the user submits this text field.

## See Also

### Creating a text field with a string

- [init(_:text:)](<init(__text_).md>) — Creates a text field with a text label generated from a localized title string.
- [init(_:text:prompt:)](<init(__text_prompt_).md>) — Creates a text field with a text label generated from a localized title string resource.
