---
title: 'removeValue(at:fromPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/removevalue(at:frompropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removevalue(at:frompropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/removevalue%28at%3Afrompropertywithkey%3A%29.json'
content_hash: 'sha256:13f76560d5a30593'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# removeValue(at:fromPropertyWithKey:)

<sub>Instance Method</sub>

Removes the object at the specified index from the collection specified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeValue(at index: Int, fromPropertyWithKey key: String)
```

## Discussion

The method `removeFrom<Key>AtIndex:` is invoked if it exists. If no corresponding scripting-KVC-compliant method (`-removeFrom<Key>AtIndex:`) is found, this method invokes `-mutableArrayValueForKey:` and mutates the result.

> [!note] Note
> Prior to OS X version 10.4, this method did not invoke `-mutableArrayValueForKey:`.

## See Also

### Indexed access

- [- insertValue:atIndex:inPropertyWithKey:](<insertvalue(__at_inpropertywithkey_).md>) — Inserts an object at the specified index in the collection specified by the passed key.
- [- replaceValueAtIndex:inPropertyWithKey:withValue:](<replacevalue(at_inpropertywithkey_withvalue_).md>) — Replaces the object at the specified index in the collection specified by the passed key.
- [- valueAtIndex:inPropertyWithKey:](<value(at_inpropertywithkey_).md>) — Retrieves an indexed object from the collection specified by the passed key.
