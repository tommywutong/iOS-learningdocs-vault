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
doc_path: '/documentation/swiftdata/persistentmodel/setvalue(forkey:to:)-3mmp2'
source_url: 'https://developer.apple.com/documentation/swiftdata/persistentmodel/setvalue(forkey:to:)-3mmp2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/persistentmodel/setvalue%28forkey%3Ato%3A%29-3mmp2.json'
content_hash: 'sha256:ddb0f783b94436cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [PersistentModel](../persistentmodel.md)

# setValue(forKey:to:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue<Value, OtherModel>(forKey: KeyPath<Self, Value>, to newValue: Value) where Value : RelationshipCollection, OtherModel == Value.PersistentElement
```

## See Also

### Modifying a value by key path

- [setValue(forKey:to:)](<setvalue(forkey_to_)-18176.md>)
- [setValue(forKey:to:)](<setvalue(forkey_to_)-3uqwc.md>)
- [setValue(forKey:to:)](<setvalue(forkey_to_)-8wepb.md>)
- [setValue(forKey:to:)](<setvalue(forkey_to_)-xt24.md>)
- [setTransformableValue(forKey:to:)](<settransformablevalue(forkey_to_).md>)
