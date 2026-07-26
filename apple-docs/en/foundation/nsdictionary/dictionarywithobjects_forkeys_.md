---
title: 'dictionaryWithObjects:forKeys:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/dictionarywithobjects:forkeys:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithobjects:forkeys:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionarywithobjects%3Aforkeys%3A.json'
content_hash: 'sha256:29a5609b79391bd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionaryWithObjects:forKeys:

<sub>Type Method</sub>

Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dictionaryWithObjects:(NSArray<id> *) objects forKeys:(NSArray<id<NSCopying>> *) keys;
```

## Parameters

- `objects` — An array containing the values for the new dictionary.

- `keys` — An array containing the keys for the new dictionary. Each key is copied (using [- copyWithZone:](<../nscopying/copy(with_).md>); keys must conform to the `NSCopying` protocol), and the copy is added to the dictionary.

## Return Value

A new dictionary containing entries constructed from the contents of `objects` and `keys`.

## Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if objects and keys don’t have the same number of elements.

## See Also

### Creating a Dictionary from Objects and Keys

- [dictionaryWithObjects:forKeys:count:](dictionarywithobjects_forkeys_count_.md) — Creates a dictionary containing a specified number of objects from a C array.
- [- initWithObjects:forKeys:](<init(objects_forkeys_).md>) — Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [- initWithObjects:forKeys:count:](<init(objects_forkeys_count_).md>) — Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [dictionaryWithObjectsAndKeys:](dictionarywithobjectsandkeys_.md) — Creates a dictionary containing entries constructed from the specified set of values and keys.
- [initWithObjectsAndKeys:](initwithobjectsandkeys_.md) — Initializes a newly allocated dictionary with entries constructed from the specified set of values and keys.
- [+ dictionaryWithObject:forKey:](<init(object_forkey_).md>) — Creates a dictionary containing a given key and value.
