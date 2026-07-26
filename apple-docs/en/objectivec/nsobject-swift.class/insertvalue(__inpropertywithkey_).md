---
title: 'insertValue(_:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/insertvalue(_:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/insertvalue(_:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/insertvalue%28_%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:c5c0bf70461c4a84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# insertValue(_:inPropertyWithKey:)

<sub>Instance Method</sub>

Inserts an object in the collection specified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func insertValue(_ value: Any, inPropertyWithKey key: String)
```

## Discussion

The method `insertIn<Key>:` is used if it exists. Otherwise, raises an `NSUndefinedKeyException`. This is part of Cocoa’s scripting support for inserting newly-created objects into containers without explicitly specifying a location.

## See Also

### Access by name, key, or ID

- [- valueWithName:inPropertyWithKey:](<value(withname_inpropertywithkey_).md>) — Retrieves a named object from the collection specified by the passed key.
- [- valueWithUniqueID:inPropertyWithKey:](<value(withuniqueid_inpropertywithkey_).md>) — Retrieves an object by ID from the collection specified by the passed key.
