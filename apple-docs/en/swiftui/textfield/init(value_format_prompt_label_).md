---
title: 'init(value:format:prompt:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/textfield/init(value:format:prompt:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/textfield/init(value:format:prompt:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textfield/init%28value%3Aformat%3Aprompt%3Alabel%3A%29.json'
content_hash: 'sha256:a0e6805227c09a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextField](../textfield.md)

# init(value:format:prompt:label:)

<sub>Initializer</sub>

Creates a text field that applies a format style to a bound value, with a label generated from a content builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<F>(value: Binding<F.FormatInput>, format: F, prompt: Text? = nil, @ContentBuilder label: () -> Label) where F : ParseableFormatStyle, F.FormatOutput == String
```

## Parameters

- `value` — The underlying value to edit.

- `format` — A format style of type `F` to use when converting between the string the user edits and the underlying value of type `F.FormatInput`. If `format` can’t perform the conversion, the text field leaves the value unchanged. If the user stops editing the text in an invalid state, the text field updates the field’s text to the last known valid value.

- `prompt` — A `Text` which provides users with guidance on what to type into the text field.

- `label` — A content builder that produces a label for the text field, describing its purpose.

## Discussion

Use this initializer to create a text field that binds to a bound value, using a [ParseableFormatStyle](../../foundation/parseableformatstyle.md) to convert to and from this type. Changes to the bound value update the string displayed by the text field. Editing the text field updates the bound value, as long as the format style can parse the text. If the format style can’t parse the input, the bound value remains unchanged.

Use the [onSubmit(of:_:)](<../view/onsubmit(of___).md>) modifier to invoke an action whenever the user submits this text field.

The following example uses a [Double](../../swift/double.md) as the bound value, and a [FloatingPointFormatStyle](../../foundation/floatingpointformatstyle.md) instance to convert to and from a string representation. As the user types, the bound value updates, which in turn updates three [Text](../text.md) views that use different format styles. If the user enters text that doesn’t represent a valid `Double`, the bound value doesn’t update.

```swift
@State private var myDouble: Double = 0.673
var body: some View {
    VStack {
        TextField(
            value: $myDouble,
            format: .number
        ) {
            Text("Double")
        }
        Text(myDouble, format: .number)
        Text(myDouble, format: .number.precision(.significantDigits(5)))
        Text(myDouble, format: .number.notation(.scientific))
    }
}
```

![A text field with the string 0.673. Below this, three text views](../../../../attachments/e225c5567dcc84af2e36e44ff5cc3768/TextField-init-format-1@2x.png)

## See Also

### Creating a text field with a value

- [init(_:value:format:prompt:)](<init(__value_format_prompt_).md>) — Creates a text field that applies a format style to a bound value, with a label generated from a localized title string resource.
- [init(_:value:formatter:)](<init(__value_formatter_).md>) — Create an instance which binds over an arbitrary type, `V`.
- [init(_:value:formatter:prompt:)](<init(__value_formatter_prompt_).md>) — Creates a text field that applies a formatter to a bound value, with a label generated from a localized title string resource.
- [init(value:formatter:prompt:label:)](<init(value_formatter_prompt_label_).md>) — Creates a text field that applies a formatter to a bound optional value, with a label generated from a content builder.
