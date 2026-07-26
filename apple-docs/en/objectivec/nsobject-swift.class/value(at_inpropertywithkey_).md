---
title: 'value(at:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(at:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(at:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28at%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:e2592098597b7218'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(at:inPropertyWithKey:)

<sub>Instance Method</sub>

Retrieves an indexed object from the collection specified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func value(at index: Int, inPropertyWithKey key: String) -> Any?
```

## Discussion

This actually works with a single-value key as well if `index` is 0. The method `valueIn<Key>AtIndex:` is used if it exists.

## See Also

### Indexed access

- [- insertValue:atIndex:inPropertyWithKey:](<insertvalue(__at_inpropertywithkey_).md>) — Inserts an object at the specified index in the collection specified by the passed key.
- [- removeValueAtIndex:fromPropertyWithKey:](<removevalue(at_frompropertywithkey_).md>) — Removes the object at the specified index from the collection specified by the passed key.
- [- replaceValueAtIndex:inPropertyWithKey:withValue:](<replacevalue(at_inpropertywithkey_withvalue_).md>) — Replaces the object at the specified index in the collection specified by the passed key.
