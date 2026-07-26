---
title: LinearGaugeStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/lineargaugestyle
source_url: 'https://developer.apple.com/documentation/swiftui/lineargaugestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/lineargaugestyle.json'
content_hash: 'sha256:5b4958bf20904c2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LinearGaugeStyle

<sub>Structure</sub>

A gauge style that displays a bar with a marker that appears at a point along the bar to indicate the gauge’s current value.

<sub>watchOS</sub>

```swift
nonisolated struct LinearGaugeStyle
```

## Overview

Use [linear](gaugestyle/linear.md) to construct this style.

## Relationships

- **Conforms To**: [GaugeStyle](gaugestyle.md)

## Topics

### Creating the gauge style

- [init()](<lineargaugestyle/init().md>) — Creates a linear gauge style.

### Deprecated initializers

- [init(tint:)](<lineargaugestyle/init(tint_).md>) — Creates a linear gauge style with a tint color. _(deprecated)_

## See Also

### Supporting types

- [DefaultGaugeStyle](defaultgaugestyle.md) — The default gauge view style in the current context of the view being styled.
- [CircularGaugeStyle](circulargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularGaugeStyle](accessorycirculargaugestyle.md) — A gauge style that displays an open ring with a marker that appears at a point along the ring to indicate the gauge’s current value.
- [AccessoryCircularCapacityGaugeStyle](accessorycircularcapacitygaugestyle.md) — A gauge style that displays a closed ring that’s partially filled in to indicate the gauge’s current value.
- [LinearCapacityGaugeStyle](linearcapacitygaugestyle.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
- [AccessoryLinearGaugeStyle](accessorylineargaugestyle.md) — A gauge style that displays bar with a marker that appears at a point along the bar to indicate the gauge’s current value.
- [AccessoryLinearCapacityGaugeStyle](accessorylinearcapacitygaugestyle.md) — A gauge style that displays bar that fills from leading to trailing edges as the gauge’s current value increases.
