---
title: 'init(_:value:total:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/progressview/init(_:value:total:)'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(_:value:total:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28_%3Avalue%3Atotal%3A%29.json'
content_hash: 'sha256:75812cc0147fa953'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(_:value:total:)

<sub>Initializer</sub>

Creates a progress view for showing determinate progress that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<V>(_ titleResource: LocalizedStringResource, value: V?, total: V = 1.0) where Label == Text, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint
```

## Parameters

- `titleResource` — Text resource for the progress view’s localized title that describes the task in progress.

- `value` — The completed amount of the task to this point, in a range of `0.0` to `total`, or `nil` if the progress is indeterminate.

- `total` — The full amount representing the complete scope of the task, meaning the task is complete if `value` equals `total`. The default value is `1.0`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the progress view pins the value to those limits, rounding to the nearest possible bound. A value of `nil` represents indeterminate progress, in which case the progress view ignores `total`.

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings. To initialize a determinate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.

## See Also

### Creating a determinate progress view

- [init(_:)](<init(__)-l5vj.md>) — Creates a progress view for visualizing the given progress instance.
- [init(value:total:)](<init(value_total_).md>) — Creates a progress view for showing determinate progress.
- [init(value:total:label:)](<init(value_total_label_).md>) — Creates a progress view for showing determinate progress, with a custom label.
- [init(value:total:label:currentValueLabel:)](<init(value_total_label_currentvaluelabel_).md>) — Creates a progress view for showing determinate progress, with a custom label.
