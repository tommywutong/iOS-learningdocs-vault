---
title: 'init(value:in:step:onEditingChanged:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 9.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/stepper/init(value:in:step:oneditingchanged:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/stepper/init(value:in:step:oneditingchanged:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/stepper/init%28value%3Ain%3Astep%3Aoneditingchanged%3Alabel%3A%29.json'
content_hash: 'sha256:010370ec60042768'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Stepper](../stepper.md)

# init(value:in:step:onEditingChanged:label:)

<sub>Initializer</sub>

Creates a stepper configured to increment or decrement a binding to a value using a step value and within a range of values you provide.

> [!warning] Deprecated
> Use [init(value:in:step:label:onEditingChanged:)](<init(value_in_step_label_oneditingchanged_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<V>(value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, onEditingChanged: @escaping (Bool) -> Void = { _ in }, @ContentBuilder label: () -> Label) where V : Strideable
```

## Parameters

- `value` — A [Binding](../binding.md) to a value that you provide.

- `bounds` — A closed range that describes the upper and lower bounds permitted by the stepper.

- `step` — The amount to increment or decrement the stepper when the user clicks or taps the stepper’s increment or decrement buttons, respectively.

- `onEditingChanged` — A closure that’s called when editing begins and ends. For example, on iOS, the user may touch and hold the increment or decrement buttons on a stepper which causes the execution of the `onEditingChanged` closure at the start and end of the gesture.

- `label` — A view describing the purpose of this stepper.

## Discussion

Use this initializer to create a stepper that increments or decrements a binding to value by the step size you provide within the given bounds. By setting the bounds, you ensure that the value never goes below or above the lowest or highest value, respectively.

The example below shows a stepper that displays the effect of incrementing or decrementing a value with the step size of `step` with the bounds defined by `range`:

```swift
struct StepperView: View {
    @State private var value = 0
    let step = 5
    let range = 1...50

    var body: some View {
        Stepper(value: $value,
                in: range,
                step: step) {
            Text("Current: \(value) in \(range.description) " +
                 "stepping by \(step)")
        }
            .padding(10)
    }
}
```

![A view displaying a stepper with a step size of five, and a prescribed range of 1 though 50.](../../../../attachments/21941a9c414c8460cb45d5d7d33ce928/SwiftUI-Stepper-value-step-range@2x.png)

## See Also

### Deprecated initializers

- [init(value:step:onEditingChanged:label:)](<init(value_step_oneditingchanged_label_).md>) — Creates a stepper configured to increment or decrement a binding to a value using a step value you provide. _(deprecated)_
- [init(onIncrement:onDecrement:onEditingChanged:label:)](<init(onincrement_ondecrement_oneditingchanged_label_).md>) — Creates a stepper instance that performs the closures you provide when the user increments or decrements the stepper. _(deprecated)_
