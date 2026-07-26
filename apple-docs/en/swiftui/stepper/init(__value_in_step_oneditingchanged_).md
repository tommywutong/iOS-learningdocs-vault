---
title: 'init(_:value:in:step:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/stepper/init(_:value:in:step:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/stepper/init(_:value:in:step:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/stepper/init%28_%3Avalue%3Ain%3Astep%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:12edb79c79b4e5fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Stepper](../stepper.md)

# init(_:value:in:step:onEditingChanged:)

<sub>Initializer</sub>

Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<V>(_ titleResource: LocalizedStringResource, value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : Strideable
```

## Parameters

- `titleResource` — Text resource for the stepper’s localized title describing the purpose of the stepper.

- `value` — A [Binding](../binding.md) to a value that your provide.

- `bounds` — A closed range that describes the upper and lower bounds permitted by the stepper.

- `step` — The amount to increment or decrement `value` each time the user clicks or taps the stepper’s increment or decrement button, respectively. Defaults to `1`.

- `onEditingChanged` — A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a `Stepper` which causes the execution  of the `onEditingChanged` closure at the start and end of the gesture.

## Discussion

Use `Stepper(_:value:in:step:onEditingChanged:)` to create a stepper that increments or decrements a value within a specific range of values by a specific step size. In the example below, a stepper increments or decrements a binding to value over a range of `1...50` by `5` at each press of the stepper’s increment or decrement buttons:

```swift
struct StepperView: View {
    @State private var value = 0
    @State private var titleKey = "Stepper"

    let step = 5
    let range = 1...50

    var body: some View {
        VStack(spacing: 20) {
            Text("Current Stepper Value: \(value)")
            Stepper(titleKey, value: $value, in: range, step: step)
        }
    }
}
```

![A view displaying a stepper that increments or decrements within a](../../../../attachments/21941a9c414c8460cb45d5d7d33ce928/SwiftUI-Stepper-value-step-range@2x.png)

## See Also

### Creating a stepper over a range

- [init(value:in:step:label:onEditingChanged:)](<init(value_in_step_label_oneditingchanged_).md>) — Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.
- [init(value:in:step:format:label:onEditingChanged:)](<init(value_in_step_format_label_oneditingchanged_).md>) — Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide, displaying its value with an applied format style.
- [init(_:value:in:step:format:onEditingChanged:)](<init(__value_in_step_format_oneditingchanged_).md>) — Creates a stepper instance that increments and decrements a binding to a value, by a step size and within a closed range that you provide, displaying its value with an applied format style.
