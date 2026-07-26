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
doc_path: '/documentation/swiftui/progressview/init(_:)-6k5se'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(_:)-6k5se'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28_%3A%29-6k5se.json'
content_hash: 'sha256:66fd6ed8457d9405'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(_:)

<sub>Initializer</sub>

Creates a progress view for showing indeterminate progress that generates its label from a localized string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey) where Label == Text
```

## Parameters

- `titleKey` — The key for the progress view’s localized title that describes the task in progress.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See [Text](../text.md) for more information about localizing strings. To initialize a indeterminate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.

## See Also

### Creating an indeterminate progress view

- [init()](<init().md>) — Creates a progress view for showing indeterminate progress, without a label.
- [init(label:)](<init(label_).md>) — Creates a progress view for showing indeterminate progress that displays a custom label.
- [init(_:)](<init(__)-3q5nf.md>) — Creates a progress view for showing indeterminate progress that generates its label from a string.
