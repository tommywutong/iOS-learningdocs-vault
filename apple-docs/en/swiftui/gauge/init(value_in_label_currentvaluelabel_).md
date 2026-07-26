---
title: 'init(value:in:label:currentValueLabel:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gauge/init(value:in:label:currentvaluelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gauge/init%28value%3Ain%3Alabel%3Acurrentvaluelabel%3A%29.json'
content_hash: 'sha256:cee54e7e247f8b99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gauge](../gauge.md)

# init(value:in:label:currentValueLabel:)

<sub>Initializer</sub>

Creates a gauge showing a value within a range and that describes the gauge’s purpose and current value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<V>(value: V, in bounds: ClosedRange<V> = 0...1, @ContentBuilder label: () -> Label, @ContentBuilder currentValueLabel: () -> CurrentValueLabel) where BoundsLabel == EmptyView, MarkedValueLabels == EmptyView, V : BinaryFloatingPoint
```

## Parameters

- `value` — The value to show on the gauge.

- `bounds` — The range of the valid values. Defaults to `0...1`.

- `label` — A view that describes the purpose of the gauge.

- `currentValueLabel` — A view that describes the current value of the gauge.

## Discussion

Use this method to create a gauge that displays a value within a range you supply with labels that describe the purpose of the gauge and its current value. In the example below, a gauge using the [circular](../gaugestyle/circular.md) style shows its current value of `67` along with a label describing the (BPM) for the gauge:

```swift
struct SimpleGauge: View {
    @State private var current = 67.0

    var body: some View {
        Gauge(value: current, in: 0...170) {
            Text("BPM")
        } currentValueLabel: {
            Text("\(current)")
        }
        .gaugeStyle(.circular)
   }
}
```

![A screenshot showing a circular gauge describing heart rate in beats](../../../../attachments/e39aab1677b1eba8885745e659503b54/SwiftUI-Gauge-LabelCurrentValueCircular@2x.png)

## See Also

### Creating a gauge

- [init(value:in:label:)](<init(value_in_label_).md>) — Creates a gauge showing a value within a range and describes the gauge’s purpose and current value.
- [init(value:in:label:currentValueLabel:markedValueLabels:)](<init(value_in_label_currentvaluelabel_markedvaluelabels_).md>) — Creates a gauge representing a value within a range.
- [init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:)](<init(value_in_label_currentvaluelabel_minimumvaluelabel_maximumvaluelabel_).md>) — Creates a gauge showing a value within a range and describes the gauge’s current, minimum, and maximum values.
- [init(value:in:label:currentValueLabel:minimumValueLabel:maximumValueLabel:markedValueLabels:)](<init(value_in_label_currentvaluelabel_minimumvaluelabel_maximumvaluelabel_markedvaluelabels_).md>) — Creates a gauge representing a value within a range.
