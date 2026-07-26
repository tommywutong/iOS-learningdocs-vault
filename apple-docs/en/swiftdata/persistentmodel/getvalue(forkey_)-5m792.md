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
doc_path: '/documentation/swiftdata/persistentmodel/getvalue(forkey:)-5m792'
source_url: 'https://developer.apple.com/documentation/swiftdata/persistentmodel/getvalue(forkey:)-5m792'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/persistentmodel/getvalue%28forkey%3A%29-5m792.json'
content_hash: 'sha256:9f00c64330b9ff44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [PersistentModel](../persistentmodel.md)

# getValue(forKey:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getValue<Value, OtherModel>(forKey: KeyPath<Self, Value>) -> Value where Value : RelationshipCollection, OtherModel == Value.PersistentElement
```

## See Also

### Accessing a value by key path

- [getValue(forKey:)](<getvalue(forkey_)-299oe.md>)
- [getValue(forKey:)](<getvalue(forkey_)-3o59k.md>)
- [getValue(forKey:)](<getvalue(forkey_)-4cs0c.md>)
- [getValue(forKey:)](<getvalue(forkey_)-998oq.md>)
- [getTransformableValue(forKey:)](<gettransformablevalue(forkey_).md>)
