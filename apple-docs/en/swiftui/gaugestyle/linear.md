---
title: linear
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gaugestyle/linear
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyle/linear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyle/linear.json'
content_hash: 'sha256:471a12f6239b3506'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GaugeStyle](../gaugestyle.md)

# linear

<sub>Type Property</sub>

A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.

<sub>watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var linear: LinearGaugeStyle { get }
```

## Discussion

Apply this style to a [Gauge](../gauge.md) or to a view hierarchy that contains gauges using the [gaugeStyle(_:)](<../view/gaugestyle(__).md>) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.linear)
```

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you create the gauge, they appear on leading and trailing edges of the bar, respectively. Otherwise, the gauge displays the `currentValueLabel` value on the leading edge.

## See Also

### Getting linear gauge styles

- [linearCapacity](linearcapacity.md) — A gauge style that displays a bar that fills from leading to trailing edges as the gauge’s current value increases.
- [accessoryLinear](accessorylinear.md) — A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [accessoryLinearCapacity](accessorylinearcapacity.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
