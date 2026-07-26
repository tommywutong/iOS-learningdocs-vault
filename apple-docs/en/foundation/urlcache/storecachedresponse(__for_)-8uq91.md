---
title: 'storeCachedResponse(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/storecachedresponse(_:for:)-8uq91'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/storecachedresponse(_:for:)-8uq91'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/storecachedresponse%28_%3Afor%3A%29-8uq91.json'
content_hash: 'sha256:2cf35d7eb0092a81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# storeCachedResponse(_:for:)

<sub>Instance Method</sub>

Stores a cached URL response for a specified data task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func storeCachedResponse(_ cachedResponse: CachedURLResponse, for dataTask: URLSessionDataTask)
```

## Parameters

- `cachedResponse` — The cached URL response to store for this data task.

- `dataTask` — The data task whose response is to be cached.

## See Also

### Getting and storing cached objects

- [- cachedResponseForRequest:](<cachedresponse(for_).md>) — Returns the cached URL response in the cache for the specified URL request.
- [- storeCachedResponse:forRequest:](<storecachedresponse(__for_)-7p7bl.md>) — Stores a cached URL response for a specified request.
- [- getCachedResponseForDataTask:completionHandler:](<getcachedresponse(for_completionhandler_).md>) — Gets the cached URL response for a data task, passing it to the provided completion handler.
