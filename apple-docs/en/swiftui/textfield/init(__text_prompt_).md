---
title: 'init(_:text:prompt:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textfield/init(_:text:prompt:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:text:prompt:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Atext%3Aprompt%3A%29.json'
content_hash: 'sha256:43c8027242918ec1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:text:prompt:)

<sub>Initializer</sub>

Creates a text field with a text label generated from a localized title string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>, prompt: Text?)
```

## Parameters

- `titleResource` — The localized title of the text field, describing its purpose.

- `text` — The text to display and edit.

- `prompt` — A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.

## Discussion

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever the user submits this text field.

## See Also

### Creating a text field with a string

- [init(_:text:)](<init(__text_).md>) — Creates a text field with a text label generated from a localized title string.
- [init(text:prompt:label:)](<init(text_prompt_label_).md>) — Creates a text field with a prompt generated from a `Text`.
