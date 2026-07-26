---
title: 'getValue(forKey:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/backingdata/getvalue(forkey:)-209t6'
source_url: 'https://developer.apple.com/documentation/swiftdata/backingdata/getvalue(forkey:)-209t6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/backingdata/getvalue%28forkey%3A%29-209t6.json'
content_hash: 'sha256:a54edaa960f2d105'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [BackingData](../backingdata.md)

# getValue(forKey:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getValue<Value, OtherModel>(forKey: KeyPath<Self.Model, Value>) -> Value where Value : RelationshipCollection, OtherModel == Value.PersistentElement
```
