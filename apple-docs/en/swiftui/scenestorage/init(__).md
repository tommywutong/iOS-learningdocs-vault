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
doc_path: '/documentation/swiftui/scenestorage/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scenestorage/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenestorage/init%28_%3A%29.json'
content_hash: 'sha256:cd1841372f28b286'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneStorage](../scenestorage.md)

# init(_:)

<sub>Initializer</sub>

Creates a property that can save and restore an Optional boolean.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ key: String) where Value == Bool?
```

## Parameters

- `key` — A key used to save and restore the value.

## Discussion

Defaults to nil if there is no restored value

## See Also

### Storing a value

- [init(wrappedValue:_:)](<init(wrappedvalue___).md>) — Creates a property that can save and restore an integer, transforming it to a `RawRepresentable` data type.
