---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/subscript(_:)-52n56'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/subscript(_:)-52n56'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/subscript%28_%3A%29-52n56.json'
content_hash: 'sha256:cb31c813cbc65adc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(key: any NSCopying) -> Any? { get }
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(key: any NSCopying) -> Any? { get set }
```

## Parameters

- `key` — The key for which to return the corresponding value.

## Return Value

The value associated with `key`, or `nil` if no value is associated with `aKey`.

## Discussion

This method has the same behavior as the [- objectForKey:](<object(forkey_).md>) method.

You shouldn’t need to call this method directly. Instead, this method is called when accessing an object by key using subscripting.

```objc
id value = dictionary[@"key"]; // equivalent to [dictionary objectForKeyedSubscript:@"key"]
```

## See Also

### Accessing Keys and Values

- [allKeys](allkeys.md) — A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [- allKeysForObject:](<allkeys(for_).md>) — Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [allValues](allvalues.md) — A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [- valueForKey:](<value(forkey_).md>) — Returns the value associated with a given key.
- [- objectsForKeys:notFoundMarker:](<objects(forkeys_notfoundmarker_).md>) — Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [- objectForKey:](<object(forkey_).md>) — Returns the value associated with a given key.
- [subscript(_:)](<subscript(__)-1bt1b.md>) — Accesses the value associated with a given key.
