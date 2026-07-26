---
title: 'object(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/object(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/object(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/object%28forkey%3A%29.json'
content_hash: 'sha256:eb350a21d3e73afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# object(forKey:)

<sub>Instance Method</sub>

Returns the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object(forKey aKey: Any) -> Any?
```

## Parameters

- `aKey` — The key for which to return the corresponding value.

## Return Value

The value associated with `aKey`, or `nil` if no value is associated with `aKey`.

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
- [subscript(_:)](<subscript(__)-1bt1b.md>) — Accesses the value associated with a given key.
