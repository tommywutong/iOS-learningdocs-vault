---
title: 'removeObject(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmaptable/removeobject(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/removeobject(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/removeobject%28forkey%3A%29.json'
content_hash: 'sha256:b200a78b1ba59ae0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# removeObject(forKey:)

<sub>Instance Method</sub>

Removes a given key and its associated value from the map table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObject(forKey aKey: KeyType?)
```

## Parameters

- `aKey` — The key to remove.

## Discussion

Does nothing if `aKey` does not exist.

## See Also

### Manipulating Content

- [- setObject:forKey:](<setobject(__forkey_).md>) — Adds a given key-value pair to the map table.
- [- removeAllObjects](<removeallobjects().md>) — Empties the map table of its entries.
