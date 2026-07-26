---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/groupedformstyle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/groupedformstyle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupedformstyle/init%28%29.json'
content_hash: 'sha256:2e36ff005cdcfed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GroupedFormStyle](../groupedformstyle.md)

# init()

<sub>Initializer</sub>

Creates a form style with scrolling, grouped rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init()
```

## Discussion

Don’t call this initializer directly. Instead, use the [grouped](../formstyle/grouped.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.grouped)
```
