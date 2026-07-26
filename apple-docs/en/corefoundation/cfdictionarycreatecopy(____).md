---
title: 'CFDictionaryCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdictionarycreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarycreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarycreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:d5169e9115c068a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryCreateCopy(_:_:)

<sub>Function</sub>

Creates and returns a new immutable dictionary with the key-value pairs of another dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDictionaryCreateCopy(_ allocator: CFAllocator!, _ theDict: CFDictionary!) -> CFDictionary!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new dictionary. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `theDict` — The dictionary to copy. The keys and values from the dictionary are copied as pointers into the new dictionary. However, the keys and values are also retained by the new dictionary. The count of the new dictionary is the same as the count of `theDict`. The new dictionary uses the same callbacks as `theDict`.

## Return Value

A new dictionary that contains the same key-value pairs as `theDict`, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a dictionary

- [CFDictionaryCreate](<cfdictionarycreate(____________).md>) — Creates an immutable dictionary containing the specified key-value pairs.
