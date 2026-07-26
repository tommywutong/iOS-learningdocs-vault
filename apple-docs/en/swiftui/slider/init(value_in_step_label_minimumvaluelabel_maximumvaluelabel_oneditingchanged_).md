---
title: 'init(value:in:step:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/slider/init(value:in:step:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slider/init(value:in:step:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slider/init%28value%3Ain%3Astep%3Alabel%3Aminimumvaluelabel%3Amaximumvaluelabel%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:279c0b06a71db5d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Slider](../slider.md)

# init(value:in:step:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)

<sub>Initializer</sub>

Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<V>(value: Binding<V>, in bounds: ClosedRange<V>, step: V.Stride = 1, @ContentBuilder label: () -> Label, @ContentBuilder minimumValueLabel: () -> ValueLabel, @ContentBuilder maximumValueLabel: () -> ValueLabel, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

## Parameters

- `value` — The selected value within `bounds`.

- `bounds` — The range of the valid values.

- `step` — The distance between each valid value.

- `label` — A `View` that describes the purpose of the instance. Not all slider styles show the label, but even in those cases, SwiftUI uses the label for accessibility. For example, VoiceOver uses the label to identify the purpose of the slider.

- `minimumValueLabel` — A view that describes `bounds.lowerBound`.

- `maximumValueLabel` — A view that describes `bounds.upperBound`.

- `onEditingChanged` — A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example, on iOS, editing begins when the user starts to drag the thumb along the slider’s track.

## See Also

### Creating a slider with labels

- [init(value:in:label:onEditingChanged:)](<init(value_in_label_oneditingchanged_).md>) — Creates a slider to select a value from a given range, which displays the provided label.
- [init(value:in:step:label:onEditingChanged:)](<init(value_in_step_label_oneditingchanged_).md>) — Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.
- [init(value:in:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)](<init(value_in_label_minimumvaluelabel_maximumvaluelabel_oneditingchanged_).md>) — Creates a slider to select a value from a given range, which displays the provided labels.
