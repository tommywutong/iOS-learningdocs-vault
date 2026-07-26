---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/subscript(_:)-1bt1b'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/subscript(_:)-1bt1b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/subscript%28_%3A%29-1bt1b.json'
content_hash: 'sha256:24a673a03035e1c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@objc dynamic subscript(key: Any) -> Any? { get }
```

## Parameters

- `key` — The key whose value you want to retrieve.

## Discussion

The returned value is `nil` if `key` does not exist in the dictionary.

The listing below creates a new dictionary. It prints the value of a key found in the dictionary (`"Coral"`) and a key not found in the dictionary (`"Cerise"`).

```swift
var hues = NSDictionary(dictionary: ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156])
print(hues["Coral"])
// Prints "Optional(16)"
print(hues["Cerise"])
// Prints "nil"

```

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [- objectForKeyedSubscript:](<subscript(__)-52n56.md>) — Returns the value associated with a given key.
