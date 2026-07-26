---
title: 'gaugeStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/gaugestyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/gaugestyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/gaugestyle%28_%3A%29.json'
content_hash: 'sha256:e742030aba3c99cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# gaugeStyle(_:)

<sub>Instance Method</sub>

Sets the style for gauges within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func gaugeStyle<S>(_ style: S) -> some View where S : GaugeStyle

```

## See Also

### Indicating a value

- [Gauge](../gauge.md) — A view that shows a value within a range.
- [ProgressView](../progressview.md) — A view that shows the progress toward completion of a task.
- [progressViewStyle(_:)](<progressviewstyle(__).md>) — Sets the style for progress views in this view.
- [DefaultDateProgressLabel](../defaultdateprogresslabel.md) — The default type of the current value label when used by a date-relative progress view.
- [DefaultButtonLabel](../defaultbuttonlabel.md) — The default label to use for a button.
