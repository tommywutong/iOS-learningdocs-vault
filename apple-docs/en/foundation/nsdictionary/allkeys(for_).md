---
title: 'allKeys(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/allkeys(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/allkeys(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/allkeys%28for%3A%29.json'
content_hash: 'sha256:f6778db33cb7d552'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# allKeys(for:)

<sub>Instance Method</sub>

Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allKeys(for anObject: Any) -> [Any]
```

## Parameters

- `anObject` — The value to look for in the dictionary.

## Return Value

A new array containing the keys corresponding to all occurrences of `anObject` in the dictionary. If no object matching `anObject` is found, returns an empty array.

## Discussion

Each object in the dictionary is sent an [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) message to determine if it’s equal to `anObject`.

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
- [subscript(_:)](<subscript(__)-1bt1b.md>) — Accesses the value associated with a given key.
