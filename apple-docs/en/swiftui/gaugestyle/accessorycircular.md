---
title: accessoryCircular
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gaugestyle/accessorycircular
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyle/accessorycircular'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyle/accessorycircular.json'
content_hash: 'sha256:6c96959c571e3659'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GaugeStyle](../gaugestyle.md)

# accessoryCircular

<sub>Type Property</sub>

A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var accessoryCircular: AccessoryCircularGaugeStyle { get }
```

## Discussion

Apply this style to a [Gauge](../gauge.md) or to a view hierarchy that contains gauges using the [gaugeStyle(_:)](<../view/gaugestyle(__).md>) modifier:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.accessoryCircular)
```

This style displays the gauge’s `currentValueLabel` value at the center of the gauge. If you provide `minimumValueLabel` and `maximumValueLabel` parameters when you create the gauge, they appear in the opening at the bottom of the ring. Otherwise, the gauge places its label in that location.

## See Also

### Getting circular gauge styles

- [circular](circular.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [accessoryCircularCapacity](accessorycircularcapacity.md) — A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
