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
doc_path: '/documentation/swiftui/scenestorage/init(wrappedvalue:_:store:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:store:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenestorage/init%28wrappedvalue%3A_%3Astore%3A%29.json'
content_hash: 'sha256:4f14bfdd519b20e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneStorage](../scenestorage.md)

# init(wrappedValue:_:store:)

<sub>Initializer</sub>

Creates a property that can save and restore tab sidebar customizations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(wrappedValue: Value = TabViewCustomization(), _ key: String, store: UserDefaults? = nil) where Value == TabViewCustomization
```

## Parameters

- `wrappedValue` — The default value if the customization is not available for the given key.

- `key` — A key used to save and restore the value.

## Discussion

You can set this customization on the TabView using [tabViewCustomization(_:)](<../view/tabviewcustomization(__).md>).

The tab view customization is typically not added to `SceneStorage`, but instead stored in `AppStorage` so the customizations are consistent across different scenes.
