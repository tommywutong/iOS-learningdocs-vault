---
title: shared
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcache/shared
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/shared.json'
content_hash: 'sha256:7b150bc81a5c313d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# shared

<sub>Type Property</sub>

The shared URL cache instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var shared: URLCache { get set }
```

## Discussion

If your app doesn’t have special caching requirements or constraints, the default shared cache instance should be acceptable. Alternatively, you can create a custom [URLCache](../urlcache.md) object and set it as the shared cache instance (use `+[NSURLCache setSharedURLCache]` in Objective-C). You should do so before making any calls to this method.

## See Also

### Related Documentation

- [Accessing cached data](../accessing-cached-data.md) — Control how URL requests make use of previously cached data.
