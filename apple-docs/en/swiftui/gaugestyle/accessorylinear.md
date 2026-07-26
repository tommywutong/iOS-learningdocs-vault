---
title: accessoryLinear
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gaugestyle/accessorylinear
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyle/accessorylinear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyle/accessorylinear.json'
content_hash: 'sha256:c742c7b44c754d58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GaugeStyle](../gaugestyle.md)

# accessoryLinear

<sub>Type Property</sub>

A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var accessoryLinear: AccessoryLinearGaugeStyle { get }
```

## Discussion

Apply this style to a [Gauge](../gauge.md) or to a view hierarchy that contains gauges using the [gaugeStyle(_:)](<../view/gaugestyle(__).md>) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.accessoryLinear)
```

If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you create the gauge, they appear on leading and trailing edges of the bar, respectively. Otherwise, the gauge displays the `currentValueLabel` value on the leading edge.

## See Also

### Getting linear gauge styles

- [linear](linear.md) — A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [linearCapacity](linearcapacity.md) — A gauge style that displays a bar that fills from leading to trailing edges as the gauge’s current value increases.
- [accessoryLinearCapacity](accessorylinearcapacity.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
