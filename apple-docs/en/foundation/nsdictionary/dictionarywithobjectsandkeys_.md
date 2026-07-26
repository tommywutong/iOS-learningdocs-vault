---
title: 'dictionaryWithObjectsAndKeys:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/dictionarywithobjectsandkeys:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithobjectsandkeys:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionarywithobjectsandkeys%3A.json'
content_hash: 'sha256:5242fdd60e223e03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionaryWithObjectsAndKeys:

<sub>Type Method</sub>

Creates a dictionary containing entries constructed from the specified set of values and keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dictionaryWithObjectsAndKeys:(id) firstObject;
```

## Parameters

- `firstObject` — The first value to add to the new dictionary.

## Discussion

After passing `firstObj`, pass a null-terminated list of alternating values and keys as variadic arguments. If any key is `nil`, an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) is raised.

This method is similar to [dictionaryWithObjects:forKeys:](dictionarywithobjects_forkeys_.md), differing only in the way key-value pairs are specified.

For example:

```objc
NSDictionary *dict = [NSDictionary dictionaryWithObjectsAndKeys:
    @"value1", @"key1", @"value2", @"key2", nil];
```

## See Also

### Creating a Dictionary from Objects and Keys

- [dictionaryWithObjects:forKeys:](dictionarywithobjects_forkeys_.md) — Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.
- [dictionaryWithObjects:forKeys:count:](dictionarywithobjects_forkeys_count_.md) — Creates a dictionary containing a specified number of objects from a C array.
- [- initWithObjects:forKeys:](<init(objects_forkeys_).md>) — Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [- initWithObjects:forKeys:count:](<init(objects_forkeys_count_).md>) — Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [initWithObjectsAndKeys:](initwithobjectsandkeys_.md) — Initializes a newly allocated dictionary with entries constructed from the specified set of values and keys.
- [+ dictionaryWithObject:forKey:](<init(object_forkey_).md>) — Creates a dictionary containing a given key and value.
