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
doc_path: /documentation/swiftui/columnsformstyle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/columnsformstyle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/columnsformstyle/init%28%29.json'
content_hash: 'sha256:db78002946bd9f9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ColumnsFormStyle](../columnsformstyle.md)

# init()

<sub>Initializer</sub>

A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init()
```

## Discussion

Don’t call this initializer directly. Instead, use the [columns](../formstyle/columns.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.columns)
```
