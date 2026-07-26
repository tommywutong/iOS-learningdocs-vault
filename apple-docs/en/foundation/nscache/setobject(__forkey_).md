---
title: 'setObject(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscache/setobject(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscache/setobject(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/setobject%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:474642cc61ade3e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# setObject(_:forKey:)

<sub>Instance Method</sub>

Sets the value of the specified key in the cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setObject(_ obj: ObjectType, forKey key: KeyType)
```

## Parameters

- `obj` — The object to be stored in the cache.

- `key` — The key with which to associate the value.

## Discussion

Unlike an `NSMutableDictionary` object, a cache does not copy the key objects that are put into it.

## See Also

### Adding and Removing Cached Values

- [- setObject:forKey:cost:](<setobject(__forkey_cost_).md>) — Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes the value of the specified key in the cache.
- [- removeAllObjects](<removeallobjects().md>) — Empties the cache.
