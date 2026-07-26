---
title: 'cache(_:willEvictObject:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscachedelegate/cache(_:willevictobject:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscachedelegate/cache(_:willevictobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscachedelegate/cache%28_%3Awillevictobject%3A%29.json'
content_hash: 'sha256:4362bd5cf9f482b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCacheDelegate](../nscachedelegate.md)

# cache(_:willEvictObject:)

<sub>Instance Method</sub>

Called when an object is about to be evicted or removed from the cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func cache(_ cache: NSCache<AnyObject, AnyObject>, willEvictObject obj: Any)
```

## Parameters

- `cache` — The cache with which the object of interest is associated.

- `obj` — The object of interest in the cache.

## Discussion

It is not possible to modify `cache` from within the implementation of this delegate method.
