---
title: 'removeObject(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscache/removeobject(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscache/removeobject(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/removeobject%28forkey%3A%29.json'
content_hash: 'sha256:767c14ddf2363fbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# removeObject(forKey:)

<sub>Instance Method</sub>

Removes the value of the specified key in the cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObject(forKey key: KeyType)
```

## Parameters

- `key` — The key identifying the value to be removed.

## See Also

### Adding and Removing Cached Values

- [- setObject:forKey:](<setobject(__forkey_).md>) — Sets the value of the specified key in the cache.
- [- setObject:forKey:cost:](<setobject(__forkey_cost_).md>) — Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.
- [- removeAllObjects](<removeallobjects().md>) — Empties the cache.
