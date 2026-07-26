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
doc_path: '/documentation/swiftui/securefield/init(_:text:prompt:)'
source_url: 'https://developer.apple.com/documentation/swiftui/securefield/init(_:text:prompt:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/securefield/init%28_%3Atext%3Aprompt%3A%29.json'
content_hash: 'sha256:057f5a6f6f517c7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SecureField](../securefield.md)

# init(_:text:prompt:)

<sub>Initializer</sub>

Creates a secure field with a prompt generated from a `Text`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>, prompt: Text?)
```

## Parameters

- `titleResource` — Text resource for the field’s localized title. The title describes the purpose of the field.

- `text` — A binding to the text that the field displays and edits.

- `prompt` — A [Text](../text.md) view that represents the secure field’s prompt. The prompt provides guidance on what people should type into the secure field.

## Discussion

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever someone submits this secure field — for example, by pressing the Return key.

## See Also

### Creating a secure text field

- [init(_:text:)](<init(__text_).md>) — Creates a secure field with a prompt generated from a `Text`.
- [init(text:prompt:label:)](<init(text_prompt_label_).md>) — Creates a secure field with a prompt generated from a `Text`.
