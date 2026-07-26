---
title: LinearCapacityGaugeStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/linearcapacitygaugestyle
source_url: 'https://developer.apple.com/documentation/swiftui/linearcapacitygaugestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/linearcapacitygaugestyle.json'
content_hash: 'sha256:374faf293533c6f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LinearCapacityGaugeStyle

<sub>Structure</sub>

A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct LinearCapacityGaugeStyle
```

## Overview

Use [linearCapacity](gaugestyle/linearcapacity.md) to construct this style.

## Relationships

- **Conforms To**: [GaugeStyle](gaugestyle.md)

## Topics

### Creating the gauge style

- [init()](<linearcapacitygaugestyle/init().md>) — Creates a linear capacity gauge style.

## See Also

### Supporting types

- [DefaultGaugeStyle](defaultgaugestyle.md) — The default gauge view style in the current context of the view being styled.
- [CircularGaugeStyle](circulargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularGaugeStyle](accessorycirculargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularCapacityGaugeStyle](accessorycircularcapacitygaugestyle.md) — A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
- [LinearGaugeStyle](lineargaugestyle.md) — A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [AccessoryLinearGaugeStyle](accessorylineargaugestyle.md) — A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [AccessoryLinearCapacityGaugeStyle](accessorylinearcapacitygaugestyle.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
