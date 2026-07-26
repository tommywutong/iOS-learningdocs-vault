---
title: 'setValue(forKey:to:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/backingdata/setvalue(forkey:to:)-rzi4'
source_url: 'https://developer.apple.com/documentation/swiftdata/backingdata/setvalue(forkey:to:)-rzi4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/backingdata/setvalue%28forkey%3Ato%3A%29-rzi4.json'
content_hash: 'sha256:cd8061fc45bcac42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [BackingData](../backingdata.md)

# setValue(forKey:to:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue<Value>(forKey: KeyPath<Self.Model, Value?>, to newValue: Value?) where Value : PersistentModel
```
