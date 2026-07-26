---
title: GaugeStyleConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gaugestyleconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyleconfiguration.json'
content_hash: 'sha256:02bd33dcf57756d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GaugeStyleConfiguration

<sub>Structure</sub>

The properties of a gauge instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct GaugeStyleConfiguration
```

## Topics

### Describing the purpose of the gauge

- [label](gaugestyleconfiguration/label-swift.property.md) — A view that describes the purpose of the gauge.
- [Label](gaugestyleconfiguration/label-swift.struct.md) — A type-erased label of a gauge, describing its purpose.

### Reporting the range

- [minimumValueLabel](gaugestyleconfiguration/minimumvaluelabel-swift.property.md) — A view that describes the minimum of the range for the current value.
- [MinimumValueLabel](gaugestyleconfiguration/minimumvaluelabel-swift.struct.md) — A type-erased value label of a gauge describing the minimum value.
- [maximumValueLabel](gaugestyleconfiguration/maximumvaluelabel-swift.property.md) — A view that describes the maximum of the range for the current value.
- [MaximumValueLabel](gaugestyleconfiguration/maximumvaluelabel-swift.struct.md) — A type-erased value label of a gauge describing the maximum value.

### Setting the value

- [value](gaugestyleconfiguration/value.md) — The current value of the gauge.
- [currentValueLabel](gaugestyleconfiguration/currentvaluelabel-swift.property.md) — A view that describes the current value.
- [CurrentValueLabel](gaugestyleconfiguration/currentvaluelabel-swift.struct.md) — A type-erased value label of a gauge that contains the current value.
- [MarkedValueLabel](gaugestyleconfiguration/markedvaluelabel.md) — A type-erased label describing a specific value of a gauge.

## See Also

### Styling indicators

- [gaugeStyle(_:)](<view/gaugestyle(__).md>) — Sets the style for gauges within this view.
- [GaugeStyle](gaugestyle.md) — Defines the implementation of all gauge instances within a view hierarchy.
- [progressViewStyle(_:)](<view/progressviewstyle(__).md>) — Sets the style for progress views in this view.
- [ProgressViewStyle](progressviewstyle.md) — A type that applies standard interaction behavior to all progress views within a view hierarchy.
- [ProgressViewStyleConfiguration](progressviewstyleconfiguration.md) — The properties of a progress view instance.
