---
title: 'init(_:text:prompt:axis:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textfield/init(_:text:prompt:axis:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:text:prompt:axis:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Atext%3Aprompt%3Aaxis%3A%29.json'
content_hash: 'sha256:8ba1481d1fa224d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:text:prompt:axis:)

<sub>Initializer</sub>

Creates a text field with a preferred axis and a text label generated from a localized title string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>, prompt: Text?, axis: Axis)
```

## Parameters

- `titleResource` — The localized title of the text field, describing its purpose.

- `text` — The text to display and edit.

- `prompt` — A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.

- `axis` — The axis in which to scroll text when it doesn’t fit in the available space.

## Discussion

Specify a preferred axis in which the text field should scroll its content when it does not fit in the available space. Depending on the style of the field, this axis may not be respected.

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever the user submits this text field.

## See Also

### Creating a scrollable text field

- [init(_:text:axis:)](<init(__text_axis_).md>) — Creates a text field with a preferred axis and a text label generated from a localized title string resource.
- [init(text:prompt:axis:label:)](<init(text_prompt_axis_label_).md>) — Creates a text field with a preferred axis and a prompt generated from a `Text`.
