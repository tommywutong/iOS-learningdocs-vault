---
title: totalCostLimit
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscache/totalcostlimit
source_url: 'https://developer.apple.com/documentation/foundation/nscache/totalcostlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/totalcostlimit.json'
content_hash: 'sha256:05c7db8f3ce5716f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# totalCostLimit

<sub>Instance Property</sub>

The maximum total cost that the cache can hold before it starts evicting objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var totalCostLimit: Int { get set }
```

## Discussion

If `0`, there is no total cost limit. The default value is `0`.

When you add an object to the cache, you may pass in a specified cost for the object, such as the size in bytes of the object. If adding this object to the cache causes the cache’s total cost to rise above `totalCostLimit`, the cache may automatically evict objects until its total cost falls below `totalCostLimit`. The order in which the cache evicts objects is not guaranteed.

This is not a strict limit, and if the cache goes over the limit, an object in the cache could be evicted instantly, at a later point in time, or possibly never, all depending on the implementation details of the cache.

## See Also

### Related Documentation

- [- setObject:forKey:cost:](<setobject(__forkey_cost_).md>) — Sets the value of the specified key in the cache, and associates the key-value pair with the specified cost.

### Managing Cache Size

- [countLimit](countlimit.md) — The maximum number of objects the cache should hold.
