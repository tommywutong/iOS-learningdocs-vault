---
title: 'init(_:text:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/securefield/init(_:text:)'
source_url: 'https://developer.apple.com/documentation/swiftui/securefield/init(_:text:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/securefield/init%28_%3Atext%3A%29.json'
content_hash: 'sha256:6039dafcced5e6bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SecureField](../securefield.md)

# init(_:text:)

<sub>Initializer</sub>

Creates a secure field with a prompt generated from a `Text`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>)
```

## Parameters

- `titleKey` — The key for the field’s localized title. The title describes the purpose of the field.

- `text` — A binding to the text that the field displays and edits.

## Discussion

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever someone submits this secure field — for example, by pressing the Return key.

## See Also

### Creating a secure text field

- [init(_:text:prompt:)](<init(__text_prompt_).md>) — Creates a secure field with a prompt generated from a `Text`.
- [init(text:prompt:label:)](<init(text_prompt_label_).md>) — Creates a secure field with a prompt generated from a `Text`.
