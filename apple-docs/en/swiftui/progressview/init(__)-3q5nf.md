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
doc_path: '/documentation/swiftui/progressview/init(_:)-3q5nf'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(_:)-3q5nf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28_%3A%29-3q5nf.json'
content_hash: 'sha256:3a00511ee26a57da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(_:)

<sub>Initializer</sub>

Creates a progress view for showing indeterminate progress that generates its label from a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<S>(_ title: S) where Label == Text, S : StringProtocol
```

## Parameters

- `title` — A string that describes the task in progress.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the title similar to [init(verbatim:)](<../text/init(verbatim_).md>). See [Text](../text.md) for more information about localizing strings. To initialize a progress view with a localized string key, use the corresponding initializer that takes a `LocalizedStringKey` instance.

## See Also

### Creating an indeterminate progress view

- [init()](<init().md>) — Creates a progress view for showing indeterminate progress, without a label.
- [init(label:)](<init(label_).md>) — Creates a progress view for showing indeterminate progress that displays a custom label.
- [init(_:)](<init(__)-6k5se.md>) — Creates a progress view for showing indeterminate progress that generates its label from a localized string.
