---
title: 'init(wrappedValue:_:store:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/appstorage/init(wrappedvalue:_:store:)'
source_url: 'https://developer.apple.com/documentation/swiftui/appstorage/init(wrappedvalue:_:store:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/appstorage/init%28wrappedvalue%3A_%3Astore%3A%29.json'
content_hash: 'sha256:c51fc47a1dbb3c8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AppStorage](../appstorage.md)

# init(wrappedValue:_:store:)

<sub>Initializer</sub>

Creates a property that can save and restore tab sidebar customizations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(wrappedValue: Value = TabViewCustomization(), _ key: String, store: UserDefaults? = nil) where Value == TabViewCustomization
```

## Parameters

- `wrappedValue` — The default value if the customization is not available for the given key.

- `key` — The key to read and write the value to in the user defaults store.

- `store` — The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.

## Discussion

You can set this customization on the TabView using [tabViewCustomization(_:)](<../view/tabviewcustomization(__).md>).

## See Also

### Storing a value

- [init(_:store:)](<init(__store_).md>) — Creates a property that can read and write an Optional boolean user default.
