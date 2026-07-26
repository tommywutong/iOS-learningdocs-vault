---
title: 'setObject(_:forKey:cost:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscache/setobject(_:forkey:cost:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscache/setobject(_:forkey:cost:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/setobject%28_%3Aforkey%3Acost%3A%29.json'
content_hash: 'sha256:f810f68ee3a06837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# setObject(_:forKey:cost:)

<sub>Instance Method</sub>

Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setObject(_ obj: ObjectType, forKey key: KeyType, cost g: Int)
```

## Parameters

- `obj` — The object to store in the cache.

- `key` — The key with which to associate the value.

- `g` — The cost with which to associate the key-value pair.

## Discussion

The `cost` value is used to compute a sum encompassing the costs of all the objects in the cache. When memory is limited or when the total cost of the cache eclipses the maximum allowed total cost, the cache could begin an eviction process to remove some of its elements. However, this eviction process is not in a guaranteed order. As a consequence, if you try to manipulate the cost values to achieve some specific behavior, the consequences could be detrimental to your program. Typically, the obvious cost is the size of the value in bytes. If that information is not readily available, you should not go through the trouble of trying to compute it, as doing so will drive up the cost of using the cache. Pass in `0` for the cost value if you otherwise have nothing useful to pass, or simply use the `setObject:forKey:` method, which does not require a `cost` value to be passed in.

Unlike an `NSMutableDictionary` object, a cache does not copy the key objects that are put into it.

## See Also

### Related Documentation

- [totalCostLimit](totalcostlimit.md) — The maximum total cost that the cache can hold before it starts evicting objects.

### Adding and Removing Cached Values

- [- setObject:forKey:](<setobject(__forkey_).md>) — Sets the value of the specified key in the cache.
- [- removeObjectForKey:](<removeobject(forkey_).md>) — Removes the value of the specified key in the cache.
- [- removeAllObjects](<removeallobjects().md>) — Empties the cache.
