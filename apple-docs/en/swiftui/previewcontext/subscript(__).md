---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/previewcontext/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/previewcontext/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewcontext/subscript%28_%3A%29.json'
content_hash: 'sha256:80de20174900dddc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreviewContext](../previewcontext.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the context’s value for a key, or a the key’s default value if the context doesn’t define a value for the key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<Key>(key: Key.Type) -> Key.Value where Key : PreviewContextKey { get }
```
