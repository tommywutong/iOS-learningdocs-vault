---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/progressview/init(_:)-l5vj'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(_:)-l5vj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28_%3A%29-l5vj.json'
content_hash: 'sha256:8f2f5a883844c1de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(_:)

<sub>Initializer</sub>

Creates a progress view for visualizing the given progress instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ progress: Progress) where Label == EmptyView, CurrentValueLabel == EmptyView
```

## Discussion

The progress view synthesizes a default label using the `localizedDescription` of the given progress instance.

## See Also

### Creating a determinate progress view

- [init(value:total:)](<init(value_total_).md>) — Creates a progress view for showing determinate progress.
- [init(_:value:total:)](<init(__value_total_).md>) — Creates a progress view for showing determinate progress that generates its label from a localized string resource.
- [init(value:total:label:)](<init(value_total_label_).md>) — Creates a progress view for showing determinate progress, with a custom label.
- [init(value:total:label:currentValueLabel:)](<init(value_total_label_currentvaluelabel_).md>) — Creates a progress view for showing determinate progress, with a custom label.
