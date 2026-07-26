---
title: 'progressViewStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/progressviewstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/progressviewstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/progressviewstyle%28_%3A%29.json'
content_hash: 'sha256:26491a006f2dcc4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# progressViewStyle(_:)

<sub>Instance Method</sub>

Sets the style for progress views in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func progressViewStyle<S>(_ style: S) -> some View where S : ProgressViewStyle

```

## Parameters

- `style` — The progress view style to use for this view.

## Discussion

For example, the following code creates a progress view that uses the “circular” style:

```swift
ProgressView()
    .progressViewStyle(.circular)
```

## See Also

### Indicating a value

- [Gauge](../gauge.md) — A view that shows a value within a range.
- [gaugeStyle(_:)](<gaugestyle(__).md>) — Sets the style for gauges within this view.
- [ProgressView](../progressview.md) — A view that shows the progress toward completion of a task.
- [DefaultDateProgressLabel](../defaultdateprogresslabel.md) — The default type of the current value label when used by a date-relative progress view.
- [DefaultButtonLabel](../defaultbuttonlabel.md) — The default label to use for a button.
