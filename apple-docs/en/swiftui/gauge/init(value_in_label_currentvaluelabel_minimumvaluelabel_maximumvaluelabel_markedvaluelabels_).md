---
title: 'init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:markedValueLabels:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:markedvaluelabels:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:minimumvaluelabel:maximumvaluelabel:markedvaluelabels:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gauge/init%28value%3Ain%3Alabel%3Acurrentvaluelabel%3Aminimumvaluelabel%3Amaximumvaluelabel%3Amarkedvaluelabels%3A%29.json'
content_hash: 'sha256:f2f9c0d72be471a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gauge](../gauge.md)

# init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:markedValueLabels:)

<sub>Initializer</sub>

Creates a gauge representing a value within a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<V>(value: V, in bounds: ClosedRange<V> = 0...1, @ContentBuilder label: () -> Label, @ContentBuilder currentValueLabel: () -> CurrentValueLabel, @ContentBuilder minimumValueLabel: () -> BoundsLabel, @ContentBuilder maximumValueLabel: () -> BoundsLabel, @ContentBuilder markedValueLabels: () -> MarkedValueLabels) where V : BinaryFloatingPoint
```

## Parameters

- `value` — The value to show in the gauge.

- `bounds` — The range of the valid values. Defaults to `0...1`.

- `label` — A view that describes the purpose of the gauge.

- `currentValueLabel` — A view that describes the current value of the gauge.

- `minimumValueLabel` — A view that describes the lower bounds of the gauge.

- `maximumValueLabel` — A view that describes the upper bounds of the gauge.

- `markedValueLabels` — A content builder containing tagged views. each of which describes a particular value of the gauge. The method ignores this parameter.

## See Also

### Creating a gauge

- [init(value:in:label:)](<init(value_in_label_).md>) — Creates a gauge showing a value within a range and describes the gauge’s purpose and current value.
- [init(value:in:label:currentValueLabel:)](<init(value_in_label_currentvaluelabel_).md>) — Creates a gauge showing a value within a range and that describes the gauge’s purpose and current value.
- [init(value:in:label:currentValueLabel:markedValueLabels:)](<init(value_in_label_currentvaluelabel_markedvaluelabels_).md>) — Creates a gauge representing a value within a range.
- [init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:)](<init(value_in_label_currentvaluelabel_minimumvaluelabel_maximumvaluelabel_).md>) — Creates a gauge showing a value within a range and describes the gauge’s current, minimum, and maximum values.
