---
title: 'insertValue(_:at:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/insertvalue(_:at:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/insertvalue(_:at:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/insertvalue%28_%3Aat%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:6acca38cae15d5eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# insertValue(_:at:inPropertyWithKey:)

<sub>Instance Method</sub>

Inserts an object at the specified index in the collection specified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)
```

## Discussion

The method `insertIn<Key>:atIndex:` is invoked if it exists. If no corresponding scripting-KVC-compliant method (`insertIn<Key>:atIndex:` ) is found, this method invokes `mutableArrayValueForKey:` and mutates the result.

> [!note] Note
> Prior to OS X version 10.4, this method did not invoke `-mutableArrayValueForKey:`.

## See Also

### Indexed access

- [- removeValueAtIndex:fromPropertyWithKey:](<removevalue(at_frompropertywithkey_).md>) — Removes the object at the specified index from the collection specified by the passed key.
- [- replaceValueAtIndex:inPropertyWithKey:withValue:](<replacevalue(at_inpropertywithkey_withvalue_).md>) — Replaces the object at the specified index in the collection specified by the passed key.
- [- valueAtIndex:inPropertyWithKey:](<value(at_inpropertywithkey_).md>) — Retrieves an indexed object from the collection specified by the passed key.
