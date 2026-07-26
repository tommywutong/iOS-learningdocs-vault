---
title: 'dictionaryWithDictionary:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/dictionarywithdictionary:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithdictionary:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionarywithdictionary%3A.json'
content_hash: 'sha256:9e1a5b147dbdbecd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionaryWithDictionary:

<sub>Type Method</sub>

Creates a dictionary containing the keys and values from another given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dictionaryWithDictionary:(NSDictionary<id,id> *) dict;
```

## Parameters

- `dict` — A dictionary containing the keys and values with which to initialize the new dictionary.

## Return Value

A new dictionary containing the keys and values found in `dict`.

## See Also

### Creating a Dictionary from Another Dictionary

- [- initWithDictionary:](<init(dictionary_)-9fw1u.md>) — Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [- initWithDictionary:copyItems:](<init(dictionary_copyitems_).md>) — Initializes a newly allocated dictionary using the objects contained in another given dictionary.
