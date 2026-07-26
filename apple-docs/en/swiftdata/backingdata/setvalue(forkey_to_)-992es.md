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
doc_path: '/documentation/swiftdata/backingdata/setvalue(forkey:to:)-992es'
source_url: 'https://developer.apple.com/documentation/swiftdata/backingdata/setvalue(forkey:to:)-992es'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/backingdata/setvalue%28forkey%3Ato%3A%29-992es.json'
content_hash: 'sha256:67f6304f334ac70a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [BackingData](../backingdata.md)

# setValue(forKey:to:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue<Value, OtherModel>(forKey: KeyPath<Self.Model, Value>, to newValue: Value) where Value : RelationshipCollection, OtherModel == Value.PersistentElement
```
