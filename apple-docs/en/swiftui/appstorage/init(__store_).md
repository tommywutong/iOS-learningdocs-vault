---
title: 'init(_:store:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/appstorage/init(_:store:)'
source_url: 'https://developer.apple.com/documentation/swiftui/appstorage/init(_:store:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/appstorage/init%28_%3Astore%3A%29.json'
content_hash: 'sha256:066999b416a23de3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AppStorage](../appstorage.md)

# init(_:store:)

<sub>Initializer</sub>

Creates a property that can read and write an Optional boolean user default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Bool?
```

## Parameters

- `key` — The key to read and write the value to in the user defaults store.

- `store` — The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.

## Discussion

Defaults to nil if there is no restored value.

## See Also

### Storing a value

- [init(wrappedValue:_:store:)](<init(wrappedvalue___store_).md>) — Creates a property that can save and restore tab sidebar customizations.
