---
title: GaugeStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gaugestyle
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyle.json'
content_hash: 'sha256:ee29c0f9cb1df283'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GaugeStyle

<sub>Protocol</sub>

Defines the implementation of all gauge instances within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol GaugeStyle
```

## Overview

To configure the style for all the [Gauge](gauge.md) instances in a view hierarchy, use the [gaugeStyle(_:)](<view/gaugestyle(__).md>) modifier. For example, you can configure a gauge to use the [circular](gaugestyle/circular.md) style:

```swift
Gauge(value: batteryLevel, in: 0...100) {
    Text("Battery Level")
}
.gaugeStyle(.circular)
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [AccessoryCircularCapacityGaugeStyle](accessorycircularcapacitygaugestyle.md), [AccessoryCircularGaugeStyle](accessorycirculargaugestyle.md), [AccessoryLinearCapacityGaugeStyle](accessorylinearcapacitygaugestyle.md), [AccessoryLinearGaugeStyle](accessorylineargaugestyle.md), [CircularGaugeStyle](circulargaugestyle.md), [DefaultGaugeStyle](defaultgaugestyle.md), [LinearCapacityGaugeStyle](linearcapacitygaugestyle.md), [LinearGaugeStyle](lineargaugestyle.md)

## Topics

### Getting the automatic style

- [automatic](gaugestyle/automatic.md) — The default gauge view style in the current context of the view being styled.

### Getting circular gauge styles

- [circular](gaugestyle/circular.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [accessoryCircular](gaugestyle/accessorycircular.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [accessoryCircularCapacity](gaugestyle/accessorycircularcapacity.md) — A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.

### Getting linear gauge styles

- [linear](gaugestyle/linear.md) — A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [linearCapacity](gaugestyle/linearcapacity.md) — A gauge style that displays a bar that fills from leading to trailing edges as the gauge’s current value increases.
- [accessoryLinear](gaugestyle/accessorylinear.md) — A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [accessoryLinearCapacity](gaugestyle/accessorylinearcapacity.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.

### Creating custom gauge styles

- [makeBody(configuration:)](<gaugestyle/makebody(configuration_).md>) — Creates a view representing the body of a gauge.
- [Configuration](gaugestyle/configuration.md) — The properties of a gauge instance.
- [Body](gaugestyle/body.md) — A view representing the body of a gauge.

### Supporting types

- [DefaultGaugeStyle](defaultgaugestyle.md) — The default gauge view style in the current context of the view being styled.
- [CircularGaugeStyle](circulargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularGaugeStyle](accessorycirculargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularCapacityGaugeStyle](accessorycircularcapacitygaugestyle.md) — A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
- [LinearGaugeStyle](lineargaugestyle.md) — A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [LinearCapacityGaugeStyle](linearcapacitygaugestyle.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
- [AccessoryLinearGaugeStyle](accessorylineargaugestyle.md) — A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [AccessoryLinearCapacityGaugeStyle](accessorylinearcapacitygaugestyle.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.

## See Also

### Styling indicators

- [gaugeStyle(_:)](<view/gaugestyle(__).md>) — Sets the style for gauges within this view.
- [GaugeStyleConfiguration](gaugestyleconfiguration.md) — The properties of a gauge instance.
- [progressViewStyle(_:)](<view/progressviewstyle(__).md>) — Sets the style for progress views in this view.
- [ProgressViewStyle](progressviewstyle.md) — A type that applies standard interaction behavior to all progress views within a view hierarchy.
- [ProgressViewStyleConfiguration](progressviewstyleconfiguration.md) — The properties of a progress view instance.
