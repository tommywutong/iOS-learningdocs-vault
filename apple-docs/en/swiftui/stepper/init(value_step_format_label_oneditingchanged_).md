---
title: 'init(value:step:format:label:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/stepper/init(value:step:format:label:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/stepper/init(value:step:format:label:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/stepper/init%28value%3Astep%3Aformat%3Alabel%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:e4c304044a6469fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Stepper](../stepper.md)

# init(value:step:format:label:onEditingChanged:)

<sub>Initializer</sub>

Creates a stepper configured to increment or decrement a binding to a value using a step value you provide, displaying its value with an applied format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride = 1, format: F, @ContentBuilder label: () -> Label, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String
```

## Parameters

- `value` — The [Binding](../binding.md) to a value that you provide.

- `step` — The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement buttons. Defaults to `1`.

- `format` — A format style of type `F` to use when converting between the string the user edits and the underlying value of type `F.FormatInput`. If `format` can’t perform the conversion, the stepper leaves `value` unchanged. If the user stops editing the text in an invalid state, the stepper updates the text to the last known valid value.

- `label` — A view describing the purpose of this stepper.

- `onEditingChanged` — A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a stepper which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.

## Discussion

Use this initializer to create a stepper that increments or decrements a bound value by a specific amount each time the user clicks or taps the stepper’s increment or decrement buttons, while displaying the current value.

In the example below, a stepper increments or decrements `value` by the `step` value of 5 at each click or tap of the control’s increment or decrement button:

```swift
struct StepperView: View {
    @State private var value = 1.0
    private let step = 5.0

    var body: some View {
        Stepper(value: $value,
                step: step,
                format: .number) {
            Text("Current value: \(value), step: \(step)")
        }
            .padding(10)
    }
}
```

![A view displaying a stepper that increments or decrements a value by](../../../../attachments/a85ed9351b703c8cc865d291ef62b2e9/SwiftUI-Stepper-value-step@2x.png)

## See Also

### Creating a stepper

- [init(value:step:label:onEditingChanged:)](<init(value_step_label_oneditingchanged_).md>) — Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.
- [init(_:value:step:onEditingChanged:)](<init(__value_step_oneditingchanged_).md>) — Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide.
- [init(_:value:step:format:onEditingChanged:)](<init(__value_step_format_oneditingchanged_).md>) — Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide, displaying its value with an applied format style.
