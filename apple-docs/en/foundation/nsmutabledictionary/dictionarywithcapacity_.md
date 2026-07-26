---
title: 'dictionaryWithCapacity:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/dictionarywithcapacity:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/dictionarywithcapacity:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/dictionarywithcapacity%3A.json'
content_hash: 'sha256:81af7b017d09fa3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# dictionaryWithCapacity:

<sub>Type Method</sub>

Creates and returns a mutable dictionary, initially giving it enough allocated memory to hold a given number of entries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dictionaryWithCapacity:(NSUInteger) numItems;
```

## Parameters

- `numItems` — The initial capacity of the new dictionary.

## Return Value

A new mutable dictionary with enough allocated memory to hold `numItems` entries.

## Discussion

Mutable dictionaries allocate additional memory as needed, so `numItems` simply establishes the object’s initial capacity.

## See Also

### Related Documentation

- [dictionary](../nsdictionary/dictionary.md) — Creates an empty dictionary.
- [dictionaryWithObjectsAndKeys:](../nsdictionary/dictionarywithobjectsandkeys_.md) — Creates a dictionary containing entries constructed from the specified set of values and keys.
- [dictionaryWithObjects:forKeys:](../nsdictionary/dictionarywithobjects_forkeys_.md) — Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [+ dictionaryWithObject:forKey:](<../nsdictionary/init(object_forkey_).md>) — Creates a dictionary containing a given key and value.
- [dictionaryWithContentsOfFile:](../nsdictionary/dictionarywithcontentsoffile_.md) — Creates a dictionary using the keys and values found in a file specified by a given path. _(deprecated)_
- [dictionaryWithObjects:forKeys:count:](../nsdictionary/dictionarywithobjects_forkeys_count_.md) — Creates a dictionary containing a specified number of objects from a C array.

### Creating and Initializing a Mutable Dictionary

- [- initWithCapacity:](<init(capacity_).md>) — Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [- init](<init().md>) — Initializes a newly allocated mutable dictionary.
- [+ dictionaryWithSharedKeySet:](<init(sharedkeyset_).md>) — Creates a mutable dictionary which is optimized for dealing with a known set of keys.
