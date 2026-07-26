---
title: 'init(value:step:label:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/stepper/init(value:step:label:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/stepper/init(value:step:label:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/stepper/init%28value%3Astep%3Alabel%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:efeca26657a58c16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Stepper](../stepper.md)

# init(value:step:label:onEditingChanged:)

<sub>Initializer</sub>

Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<V>(value: Binding<V>, step: V.Stride = 1, @ContentBuilder label: () -> Label, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

## Parameters

- `value` — The [Binding](../binding.md) to a value that you provide.

- `step` — The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement buttons. Defaults to `1`.

- `label` — A view describing the purpose of this stepper.

- `onEditingChanged` — A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a stepper which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.

## Discussion

Use this initializer to create a stepper that increments or decrements a bound value by a specific amount each time the user clicks or taps the stepper’s increment or decrement buttons.

In the example below, a stepper increments or decrements `value` by the `step` value of 5 at each click or tap of the control’s increment or decrement button:

```swift
struct StepperView: View {
    @State private var value = 1
    let step = 5
    var body: some View {
        Stepper(value: $value,
                step: step) {
            Text("Current value: \(value), step: \(step)")
        }
            .padding(10)
    }
}
```

![A view displaying a stepper that increments or decrements a value by](../../../../attachments/a85ed9351b703c8cc865d291ef62b2e9/SwiftUI-Stepper-value-step@2x.png)

## See Also

### Creating a stepper

- [init(value:step:format:label:onEditingChanged:)](<init(value_step_format_label_oneditingchanged_).md>) — Creates a stepper configured to increment or decrement a binding to a value using a step value you provide, displaying its value with an applied format style.
- [init(_:value:step:onEditingChanged:)](<init(__value_step_oneditingchanged_).md>) — Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide.
- [init(_:value:step:format:onEditingChanged:)](<init(__value_step_format_oneditingchanged_).md>) — Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide, displaying its value with an applied format style.
