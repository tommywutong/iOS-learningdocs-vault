---
title: 'CFDictionaryCreateMutableCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarycreatemutablecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarycreatemutablecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarycreatemutablecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c21cb9c2aeb156e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryCreateMutableCopy(_:_:_:)

<sub>Function</sub>

Creates a new mutable dictionary with the key-value pairs from another dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theDict: CFDictionary!) -> CFMutableDictionary!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new dictionary and its storage for key-value pairs. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `capacity` — The maximum number of key-value pairs that can be contained by the new dictionary. The dictionary starts with the same number of key-value pairs as `theDict` and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the count of `theDict`.

- `theDict` — The dictionary to copy. The keys and values from the dictionary are copied as pointers into the new dictionary, not that which the values point to (if anything). The keys and values are also retained by the new dictionary. The count of the new dictionary is the same as the count of `theDict`. The new dictionary uses the same callbacks as `theDict`.

## Return Value

A new dictionary that contains the same values as `theDict`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Mutable Dictionary

- [CFDictionaryCreateMutable](<cfdictionarycreatemutable(________).md>) — Creates a new mutable dictionary.
