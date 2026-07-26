---
title: 'objects(forKeys:notFoundMarker:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/objects(forkeys:notfoundmarker:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/objects(forkeys:notfoundmarker:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/objects%28forkeys%3Anotfoundmarker%3A%29.json'
content_hash: 'sha256:bef304dbefb1de85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# objects(forKeys:notFoundMarker:)

<sub>Instance Method</sub>

Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objects(forKeys keys: [Any], notFoundMarker marker: Any) -> [Any]
```

## Parameters

- `keys` — An `NSArray` containing the keys for which to return corresponding values.

- `marker` — The marker object to place in the corresponding element of the returned array if an object isn’t found in the dictionary to correspond to a given key.

## Discussion

The objects in the returned array and the `keys` array have a one-for-one correspondence, so that the nthe object in the returned array corresponds to the nthe key in `keys`.

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
- [subscript(_:)](<subscript(__)-1bt1b.md>) — Accesses the value associated with a given key.
