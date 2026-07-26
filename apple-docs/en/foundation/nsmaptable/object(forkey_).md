---
title: 'object(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmaptable/object(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/object(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/object%28forkey%3A%29.json'
content_hash: 'sha256:0714e50490e473b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# object(forKey:)

<sub>Instance Method</sub>

Returns a the value associated with a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object(forKey aKey: KeyType?) -> ObjectType?
```

## Parameters

- `aKey` — The key for which to return the corresponding value.

## Return Value

The value associated with `aKey`, or `nil` if no value is associated with `aKey`.

## See Also

### Accessing Content

- [- keyEnumerator](<keyenumerator().md>) — Returns an enumerator object that lets you access each key in the map table.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each value in the map table.
- [count](count.md) — The number of key-value pairs in the map table.
