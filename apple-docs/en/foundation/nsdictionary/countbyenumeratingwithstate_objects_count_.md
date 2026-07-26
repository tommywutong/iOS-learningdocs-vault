---
title: 'countByEnumeratingWithState:objects:count:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/countbyenumeratingwithstate:objects:count:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/countbyenumeratingwithstate:objects:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/countbyenumeratingwithstate%3Aobjects%3Acount%3A.json'
content_hash: 'sha256:c2a86b250d5376b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# countByEnumeratingWithState:objects:count:

<sub>Instance Method</sub>

Returns by reference a C array of objects over which the sender should iterate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSUInteger) countByEnumeratingWithState:(NSFastEnumerationState *) state objects:(K[]) buffer count:(NSUInteger) len;
```

## Parameters

- `state` — Context information that is used in the enumeration to, in addition to other possibilities, ensure that the collection has not been mutated.

- `buffer` — A C array of objects over which the sender is to iterate.

- `len` — The maximum number of objects to return in `buffer`.

## Return Value

The number of objects returned in `buffer`. Returns `0` when the iteration is finished.

## See Also

### Enumerating Dictionaries

- [- keyEnumerator](<keyenumerator().md>) — Provides an enumerator to access the keys in the dictionary.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each value in the dictionary.
- [- enumerateKeysAndObjectsUsingBlock:](<enumeratekeysandobjects(__).md>) — Applies a given block object to the entries of the dictionary.
- [- enumerateKeysAndObjectsWithOptions:usingBlock:](<enumeratekeysandobjects(options_using_).md>) — Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
