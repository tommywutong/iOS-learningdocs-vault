---
title: accessoryCircularCapacity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gaugestyle/accessorycircularcapacity
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyle/accessorycircularcapacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyle/accessorycircularcapacity.json'
content_hash: 'sha256:3b76e7d81c63e842'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GaugeStyle](../gaugestyle.md)

# accessoryCircularCapacity

<sub>Type Property</sub>

A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var accessoryCircularCapacity: AccessoryCircularCapacityGaugeStyle { get }
```

## Discussion

Apply this style to a [Gauge](../gauge.md) or to a view hierarchy that contains gauges using the [gaugeStyle(_:)](<../view/gaugestyle(__).md>) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.accessoryCircularCapacity)
```

This style displays the gauge’s `currentValueLabel` value at the center of the gauge.

## See Also

### Getting circular gauge styles

- [circular](circular.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [accessoryCircular](accessorycircular.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
