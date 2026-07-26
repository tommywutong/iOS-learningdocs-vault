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
doc_path: '/documentation/swiftdata/backingdata/getvalue(forkey:)-1pric'
source_url: 'https://developer.apple.com/documentation/swiftdata/backingdata/getvalue(forkey:)-1pric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/backingdata/getvalue%28forkey%3A%29-1pric.json'
content_hash: 'sha256:caf0fe9d597941c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [BackingData](../backingdata.md)

# getValue(forKey:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getValue<Value>(forKey: KeyPath<Self.Model, Value>) -> Value where Value : PersistentModel
```
