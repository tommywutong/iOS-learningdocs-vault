---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscache/delegate
source_url: 'https://developer.apple.com/documentation/foundation/nscache/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/delegate.json'
content_hash: 'sha256:927a3cec347bfa53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# delegate

<sub>Instance Property</sub>

The cache’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var delegate: (any NSCacheDelegate)? { get set }
```

## Discussion

The delegate must adopt the [NSCacheDelegate](../nscachedelegate.md) protocol.

## See Also

### Managing the Delegate

- [NSCacheDelegate](../nscachedelegate.md) — The delegate of an [NSCache](../nscache.md) object implements this protocol to perform specialized actions when an object is about to be evicted or removed from the cache.
