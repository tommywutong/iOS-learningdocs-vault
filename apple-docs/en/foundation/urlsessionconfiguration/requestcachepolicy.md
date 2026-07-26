---
title: requestCachePolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/requestcachepolicy
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/requestcachepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/requestcachepolicy.json'
content_hash: 'sha256:7e6ee4c29f1da350'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# requestCachePolicy

<sub>Instance Property</sub>

A predefined constant that determines when to return a response from the cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requestCachePolicy: NSURLRequest.CachePolicy { get set }
```

## Discussion

This property determines the request caching policy used by tasks within sessions based on this configuration.

Set this property to one of the constants defined in [CachePolicy](../nsurlrequest/cachepolicy-swift.enum.md) to specify whether the cache policy should depend on expiration dates and age, whether the cache should be disabled entirely, and whether the server should be contacted to determine if the content has changed since it was last requested.

The default value is [NSURLRequestUseProtocolCachePolicy](../nsurlrequest/cachepolicy-swift.enum/useprotocolcachepolicy.md).

## See Also

### Setting caching policies

- [URLCache](urlcache.md) — The URL cache for providing cached responses to requests within the session.
