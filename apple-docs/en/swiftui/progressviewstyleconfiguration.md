---
title: ProgressViewStyleConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressviewstyleconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/progressviewstyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressviewstyleconfiguration.json'
content_hash: 'sha256:cb817399aaa7dcea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ProgressViewStyleConfiguration

<sub>Structure</sub>

The properties of a progress view instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ProgressViewStyleConfiguration
```

## Topics

### Configuring the label

- [label](progressviewstyleconfiguration/label-swift.property.md) — A view that describes the task represented by the progress view.
- [Label](progressviewstyleconfiguration/label-swift.struct.md) — A type-erased label describing the task represented by the progress view.

### Configuring the current value label

- [currentValueLabel](progressviewstyleconfiguration/currentvaluelabel-swift.property.md) — A view that describes the current value of a progress view.
- [CurrentValueLabel](progressviewstyleconfiguration/currentvaluelabel-swift.struct.md) — A type-erased label that describes the current value of a progress view.

### Configuring progress completion

- [fractionCompleted](progressviewstyleconfiguration/fractioncompleted.md) — The completed fraction of the task represented by the progress view, from `0.0` (not yet started) to `1.0` (fully complete), or `nil` if the progress is indeterminate or relative to a date interval.

## See Also

### Styling indicators

- [gaugeStyle(_:)](<view/gaugestyle(__).md>) — Sets the style for gauges within this view.
- [GaugeStyle](gaugestyle.md) — Defines the implementation of all gauge instances within a view hierarchy.
- [GaugeStyleConfiguration](gaugestyleconfiguration.md) — The properties of a gauge instance.
- [progressViewStyle(_:)](<view/progressviewstyle(__).md>) — Sets the style for progress views in this view.
- [ProgressViewStyle](progressviewstyle.md) — A type that applies standard interaction behavior to all progress views within a view hierarchy.
