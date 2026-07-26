---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/progressview/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28_%3A%29.json'
content_hash: 'sha256:bad4c2853c6f4e31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(_:)

<sub>Initializer</sub>

Creates a progress view for showing indeterminate progress that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource) where Label == Text
```

## Parameters

- `titleResource` — Text resource for the progress view’s localized title that describes the task in progress.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings. To initialize a indeterminate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.
