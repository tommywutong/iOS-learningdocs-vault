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
doc_path: '/documentation/swiftui/textfield/init(_:text:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:text:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Atext%3A%29.json'
content_hash: 'sha256:1a9b9841b17695c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:text:)

<sub>Initializer</sub>

Creates a text field with a text label generated from a localized title string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, text: Binding<String>)
```

## Parameters

- `titleKey` — The key for the localized title of the text field, describing its purpose.

- `text` — The text to display and edit.

## See Also

### Creating a text field with a string

- [init(_:text:prompt:)](<init(__text_prompt_).md>) — Creates a text field with a text label generated from a localized title string resource.
- [init(text:prompt:label:)](<init(text_prompt_label_).md>) — Creates a text field with a prompt generated from a `Text`.
