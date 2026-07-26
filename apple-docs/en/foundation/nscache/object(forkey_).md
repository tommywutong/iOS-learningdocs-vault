---
title: 'object(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscache/object(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscache/object(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/object%28forkey%3A%29.json'
content_hash: 'sha256:ceed1fa049279a98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# object(forKey:)

<sub>Instance Method</sub>

Returns the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object(forKey key: KeyType) -> ObjectType?
```

## Parameters

- `key` — An object identifying the value.

## Return Value

The value associated with `key`, or `nil` if no value is associated with `key`.

## See Also

### Related Documentation

- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes the value of the specified key in the cache.
- [- setObject:forKey:cost:](<setobject(__forkey_cost_).md>) — Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [- setObject:forKey:](<setobject(__forkey_).md>) — Sets the value of the specified key in the cache.
