---
title: circular
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gaugestyle/circular
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyle/circular'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyle/circular.json'
content_hash: 'sha256:291474f918e587c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GaugeStyle](../gaugestyle.md)

# circular

<sub>Type Property</sub>

A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.

<sub>watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var circular: CircularGaugeStyle { get }
```

## Discussion

Apply this style to a [Gauge](../gauge.md) or to a view hierarchy that contains gauges using the [gaugeStyle(_:)](<../view/gaugestyle(__).md>) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.circular)
```

This style displays the gauge’s `currentValueLabel` value at the center of the gauge. If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you create the gauge, they appear in the opening at the bottom of the ring. Otherwise, the gauge places its label in that location.

## See Also

### Getting circular gauge styles

- [accessoryCircular](accessorycircular.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [accessoryCircularCapacity](accessorycircularcapacity.md) — A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
