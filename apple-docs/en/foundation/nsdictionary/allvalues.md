---
title: allValues
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/allvalues
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/allvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/allvalues.json'
content_hash: 'sha256:d51175472c873dc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# allValues

<sub>Instance Property</sub>

A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allValues: [Any] { get }
```

## Discussion

The order of the values in the array isn’t defined.

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
- [subscript(_:)](<subscript(__)-1bt1b.md>) — Accesses the value associated with a given key.
