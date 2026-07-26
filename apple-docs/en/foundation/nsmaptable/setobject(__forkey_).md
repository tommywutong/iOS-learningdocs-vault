---
title: 'setObject(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmaptable/setobject(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/setobject(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/setobject%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:500f4dda728eb2c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# setObject(_:forKey:)

<sub>Instance Method</sub>

Adds a given key-value pair to the map table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setObject(_ anObject: ObjectType?, forKey aKey: KeyType?)
```

## Parameters

- `anObject` — The value for `aKey`.

- `aKey` — The key for `anObject`.

## See Also

### Manipulating Content

- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes a given key and its associated value from the map table.
- [- removeAllObjects](<removeallobjects().md>) — Empties the map table of its entries.
