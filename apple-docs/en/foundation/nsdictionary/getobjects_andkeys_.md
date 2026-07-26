---
title: 'getObjects:andKeys:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（11.0 起废弃）, iPadOS 2.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdictionary/getobjects:andkeys:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/getobjects:andkeys:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/getobjects%3Aandkeys%3A.json'
content_hash: 'sha256:cb2a7ab6bdb7c1aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# getObjects:andKeys:

<sub>Instance Method</sub>

Returns by reference C arrays of the keys and values in the dictionary.

> [!warning] Deprecated
> Use [getObjects:andKeys:count:](getobjects_andkeys_count_.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) getObjects:(ObjectType[]) objects andKeys:(KeyType[]) keys;
```

## Parameters

- `objects` — Upon return, contains a C array of the values in the dictionary.

- `keys` — Upon return, contains a C array of the keys in the dictionary.

## Discussion

The elements in the returned array and the keys array have a one-for-one correspondence, so that the nth object in the returned array corresponds to the the key in keys.

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [getObjects:andKeys:count:](getobjects_andkeys_count_.md) — Returns by reference C arrays of the keys and values in the dictionary.
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
