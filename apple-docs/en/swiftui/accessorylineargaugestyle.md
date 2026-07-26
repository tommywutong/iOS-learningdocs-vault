---
title: AccessoryLinearGaugeStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessorylineargaugestyle
source_url: 'https://developer.apple.com/documentation/swiftui/accessorylineargaugestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessorylineargaugestyle.json'
content_hash: 'sha256:cc58a6d94c4c58c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessoryLinearGaugeStyle

<sub>Structure</sub>

A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct AccessoryLinearGaugeStyle
```

## Overview

Use [accessoryLinear](gaugestyle/accessorylinear.md) to construct this style.

## Relationships

- **Conforms To**: [GaugeStyle](gaugestyle.md)

## Topics

### Creating the gauge style

- [init()](<accessorylineargaugestyle/init().md>) — Creates an accessory linear gauge style.

## See Also

### Supporting types

- [DefaultGaugeStyle](defaultgaugestyle.md) — The default gauge view style in the current context of the view being styled.
- [CircularGaugeStyle](circulargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularGaugeStyle](accessorycirculargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularCapacityGaugeStyle](accessorycircularcapacitygaugestyle.md) — A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
- [LinearGaugeStyle](lineargaugestyle.md) — A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [LinearCapacityGaugeStyle](linearcapacitygaugestyle.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
- [AccessoryLinearCapacityGaugeStyle](accessorylinearcapacitygaugestyle.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
