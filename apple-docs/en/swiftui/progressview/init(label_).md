---
title: 'init(label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/progressview/init(label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28label%3A%29.json'
content_hash: 'sha256:121c29d2dc4bcaea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(label:)

<sub>Initializer</sub>

Creates a progress view for showing indeterminate progress that displays a custom label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder label: () -> Label)
```

## Parameters

- `label` — A content builder that creates a view that describes the task in progress.

## See Also

### Creating an indeterminate progress view

- [init()](<init().md>) — Creates a progress view for showing indeterminate progress, without a label.
- [init(_:)](<init(__)-6k5se.md>) — Creates a progress view for showing indeterminate progress that generates its label from a localized string.
- [init(_:)](<init(__)-3q5nf.md>) — Creates a progress view for showing indeterminate progress that generates its label from a string.
