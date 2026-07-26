---
title: 'value(withUniqueID:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(withuniqueid:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(withuniqueid:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28withuniqueid%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:fce36c1196ca4599'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(withUniqueID:inPropertyWithKey:)

<sub>Instance Method</sub>

Retrieves an object by ID from the collection specified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?
```

## Discussion

The method `valueIn<Key>WithUniqueID:` is invoked if it exists. Otherwise, raises an `NSUndefinedKeyException`. The declared type of `uniqueID` in the constructed method must be `id`, `NSNumber *`, `NSString *`, or one of the scalar types that can be encapsulated by `NSNumber`.

## See Also

### Access by name, key, or ID

- [- insertValue:inPropertyWithKey:](<insertvalue(__inpropertywithkey_).md>) — Inserts an object in the collection specified by the passed key.
- [- valueWithName:inPropertyWithKey:](<value(withname_inpropertywithkey_).md>) — Retrieves a named object from the collection specified by the passed key.
