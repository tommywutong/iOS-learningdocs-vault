---
title: 'value(withName:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(withname:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(withname:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28withname%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:088603662cf31b42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(withName:inPropertyWithKey:)

<sub>Instance Method</sub>

Retrieves a named object from the collection specified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func value(withName name: String, inPropertyWithKey key: String) -> Any?
```

## Discussion

The method `valueIn<Key>WithName:` is used if it exists. Otherwise, raises an `NSUndefinedKeyException`.

## See Also

### Access by name, key, or ID

- [- insertValue:inPropertyWithKey:](<insertvalue(__inpropertywithkey_).md>) — Inserts an object in the collection specified by the passed key.
- [- valueWithUniqueID:inPropertyWithKey:](<value(withuniqueid_inpropertywithkey_).md>) — Retrieves an object by ID from the collection specified by the passed key.
