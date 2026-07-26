---
title: 'init(_:text:selection:prompt:axis:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textfield/init(_:text:selection:prompt:axis:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(_:text:selection:prompt:axis:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28_%3Atext%3Aselection%3Aprompt%3Aaxis%3A%29.json'
content_hash: 'sha256:359301516f6683e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(_:text:selection:prompt:axis:)

<sub>Initializer</sub>

Creates a text field with a binding to the current selection and a text label generated from a localized title string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, text: Binding<String>, selection: Binding<TextSelection?>, prompt: Text? = nil, axis: Axis? = nil)
```

## Parameters

- `titleResource` — The localized title of the text field, describing its purpose.

- `text` — The text to display and edit.

- `selection` — A [Binding](../binding.md) to the variable containing the selection.

- `prompt` — A `Text` representing the prompt of the text field which provides users with guidance on what to type into the text field. Defaults to `nil`.

- `axis` — The axis in which to scroll text when it doesn’t fit in the available space. Defaults to `nil`.

## Discussion

The following example shows a text field with a binding to the current selection:

```swift
@State private var message: String = ""
@State private var selection: TextSelection? = nil

var body: some View {
    TextField(
        "Message",
        text: $message,
        selection: $selection
    )
}
```

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever the user submits this text field.
