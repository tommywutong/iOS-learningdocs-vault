---
title: 'value(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/value(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/value(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/value%28forkey%3A%29.json'
content_hash: 'sha256:06bcb9432b8feab0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# value(forKey:)

<sub>Instance Method</sub>

Returns the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forKey key: String) -> Any?
```

## Parameters

- `key` — The key for which to return the corresponding value. Note that when using key-value coding, the key must be a string (see [Accessing Object Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170)).

## Return Value

The value associated with `key`.

## Discussion

If `key` does not start with “`@`”, invokes [- objectForKey:](<object(forkey_).md>). If `key` does start with “`@`”, strips the “@” and invokes `[super valueForKey:]` with the rest of the key.

## See Also

### Related Documentation

- [- setValue:forKey:](<../nsmutabledictionary/setvalue(__forkey_).md>) — Adds a given key-value pair to the dictionary.

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
- [subscript(_:)](<subscript(__)-1bt1b.md>) — Accesses the value associated with a given key.
