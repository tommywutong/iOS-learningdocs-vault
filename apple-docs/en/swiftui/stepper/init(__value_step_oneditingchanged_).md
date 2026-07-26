---
title: 'init(_:value:step:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/stepper/init(_:value:step:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/stepper/init(_:value:step:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/stepper/init%28_%3Avalue%3Astep%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:7272d3382f33475c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Stepper](../stepper.md)

# init(_:value:step:onEditingChanged:)

<sub>Initializer</sub>

Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<V>(_ titleResource: LocalizedStringResource, value: Binding<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

## Parameters

- `titleResource` — Text resource for the stepper’s localized title describing the purpose of the stepper.

- `value` — A [Binding](../binding.md) to a value that you provide.

- `step` — The amount to increment or decrement `value` each time the user clicks or taps the stepper’s plus or minus button, respectively.  Defaults to `1`.

- `onEditingChanged` — A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a `Stepper` which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.

## Discussion

Use `Stepper(_:value:step:onEditingChanged:)` to create a stepper with a custom title that increments or decrements a binding to value by the step size you specify.

In the example below, the stepper increments or decrements the binding value by `5` each time the user clicks or taps on the control’s increment or decrement buttons, respectively:

```swift
struct StepperView: View {
    @State private var value = 1
    let step = 5

    var body: some View {
        Stepper("Current value: \(value), step: \(step)",
                value: $value,
                step: step)
            .padding(10)
    }
}
```

![A view displaying a stepper that increments or decrements by 5 each](../../../../attachments/a85ed9351b703c8cc865d291ef62b2e9/SwiftUI-Stepper-value-step@2x.png)

## See Also

### Creating a stepper

- [init(value:step:label:onEditingChanged:)](<init(value_step_label_oneditingchanged_).md>) — Creates a stepper configured to increment or decrement a binding to a value using a step value you provide.
- [init(value:step:format:label:onEditingChanged:)](<init(value_step_format_label_oneditingchanged_).md>) — Creates a stepper configured to increment or decrement a binding to a value using a step value you provide, displaying its value with an applied format style.
- [init(_:value:step:format:onEditingChanged:)](<init(__value_step_format_oneditingchanged_).md>) — Creates a stepper with a title key and configured to increment and decrement a binding to a value and step amount you provide, displaying its value with an applied format style.
