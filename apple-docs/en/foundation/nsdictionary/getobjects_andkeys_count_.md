---
title: 'getObjects:andKeys:count:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/getobjects:andkeys:count:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/getobjects:andkeys:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/getobjects%3Aandkeys%3Acount%3A.json'
content_hash: 'sha256:924a3568ec8cd63b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# getObjects:andKeys:count:

<sub>Instance Method</sub>

Returns by reference C arrays of the keys and values in the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) getObjects:(ObjectType[]) objects andKeys:(KeyType[]) keys count:(NSUInteger) count;
```

## Parameters

- `objects` — Upon return, contains a C array of the values in the dictionary.

- `keys` — Upon return, contains a C array of the keys in the dictionary.

- `count` — The maximum number of objects to return.

## Discussion

The elements in the returned array and the keys array have a one-for-one correspondence, so that the nth object in the returned array corresponds to the the key in keys.

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [getObjects:andKeys:](getobjects_andkeys_.md) — Returns by reference C arrays of the keys and values in the dictionary. _(deprecated)_
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
