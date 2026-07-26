---
title: 'init(text:prompt:axis:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textfield/init(text:prompt:axis:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(text:prompt:axis:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28text%3Aprompt%3Aaxis%3Alabel%3A%29.json'
content_hash: 'sha256:b914e616201951eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(text:prompt:axis:label:)

<sub>Initializer</sub>

Creates a text field with a preferred axis and a prompt generated from a `Text`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(text: Binding<String>, prompt: Text? = nil, axis: Axis, @ContentBuilder label: () -> Label)
```

## Parameters

- `text` — The text to display and edit.

- `prompt` — A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field.

- `axis` — The axis in which to scroll text when it doesn’t fit in the available space.

- `label` — A view that describes the purpose of the text field.

## Discussion

Specify a preferred axis in which the text field should scroll its content when it does not fit in the available space. Depending on the style of the field, this axis may not be respected.

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever the user submits this text field.

## See Also

### Creating a scrollable text field

- [init(_:text:axis:)](<init(__text_axis_).md>) — Creates a text field with a preferred axis and a text label generated from a localized title string resource.
- [init(_:text:prompt:axis:)](<init(__text_prompt_axis_).md>) — Creates a text field with a preferred axis and a text label generated from a localized title string resource.
