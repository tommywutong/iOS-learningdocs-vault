---
title: urlCache
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/urlcache
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/urlcache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/urlcache.json'
content_hash: 'sha256:e4b5dec6a1093a09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# urlCache

<sub>Instance Property</sub>

The URL cache for providing cached responses to requests within the session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var urlCache: URLCache? { get set }
```

## Discussion

This property determines the URL cache object used by tasks within sessions based on this configuration.

To disable caching, set this property to `nil`.

For default sessions, the default value is the shared URL cache object.

For background sessions, the default value is `nil`.

For ephemeral sessions, the default value is a private cache object that stores data in memory only, and is destroyed when you invalidate the session.

## See Also

### Setting caching policies

- [requestCachePolicy](requestcachepolicy.md) — A predefined constant that determines when to return a response from the cache.
