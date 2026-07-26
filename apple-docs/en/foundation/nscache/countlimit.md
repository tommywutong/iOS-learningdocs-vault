---
title: countLimit
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscache/countlimit
source_url: 'https://developer.apple.com/documentation/foundation/nscache/countlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/countlimit.json'
content_hash: 'sha256:a954a7a590ef22ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# countLimit

<sub>Instance Property</sub>

The maximum number of objects the cache should hold.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countLimit: Int { get set }
```

## Discussion

If `0`, there is no count limit. The default value is `0`.

This is not a strict limit—if the cache goes over the limit, an object in the cache could be evicted instantly, later, or possibly never, depending on the implementation details of the cache.

## See Also

### Managing Cache Size

- [totalCostLimit](totalcostlimit.md) — The maximum total cost that the cache can hold before it starts evicting objects.
