---
title: 'replaceValue(at:inPropertyWithKey:withValue:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/replacevalue%28at%3Ainpropertywithkey%3Awithvalue%3A%29.json'
content_hash: 'sha256:b5ff9aa9438a9c48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# replaceValue(at:inPropertyWithKey:withValue:)

<sub>Instance Method</sub>

Replaces the object at the specified index in the collection specified by the passed key.

<sub>Mac Catalyst, macOS</sub>

```swift
func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)
```

## Discussion

The method `replaceIn<Key>:atIndex:` is invoked if it exists. If no corresponding scripting-KVC-compliant method (`-replaceIn<Key>atIndex:`) is found, this method invokes `-mutableArrayValueForKey:` and mutates the result.

> [!note] Note
> Prior to OS X version 10.4, this method did not invoke `-mutableArrayValueForKey:`.

## See Also

### Indexed access

- [- insertValue:atIndex:inPropertyWithKey:](<insertvalue(__at_inpropertywithkey_).md>) — Inserts an object at the specified index in the collection specified by the passed key.
- [- removeValueAtIndex:fromPropertyWithKey:](<removevalue(at_frompropertywithkey_).md>) — Removes the object at the specified index from the collection specified by the passed key.
- [- valueAtIndex:inPropertyWithKey:](<value(at_inpropertywithkey_).md>) — Retrieves an indexed object from the collection specified by the passed key.
