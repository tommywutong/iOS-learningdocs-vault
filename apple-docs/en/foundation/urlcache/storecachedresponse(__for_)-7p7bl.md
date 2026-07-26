---
title: 'storeCachedResponse(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/storecachedresponse(_:for:)-7p7bl'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/storecachedresponse(_:for:)-7p7bl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/storecachedresponse%28_%3Afor%3A%29-7p7bl.json'
content_hash: 'sha256:494237cd8a44880b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# storeCachedResponse(_:for:)

<sub>Instance Method</sub>

Stores a cached URL response for a specified request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func storeCachedResponse(_ cachedResponse: CachedURLResponse, for request: URLRequest)
```

## Parameters

- `cachedResponse` — The cached URL response to store.

- `request` — The request for which the cached URL response is being stored.

## Discussion

If you override this method, you should also override [- storeCachedResponse:forDataTask:](<storecachedresponse(__for_)-8uq91.md>).

## See Also

### Getting and storing cached objects

- [- cachedResponseForRequest:](<cachedresponse(for_).md>) — Returns the cached URL response in the cache for the specified URL request.
- [- getCachedResponseForDataTask:completionHandler:](<getcachedresponse(for_completionhandler_).md>) — Gets the cached URL response for a data task, passing it to the provided completion handler.
- [- storeCachedResponse:forDataTask:](<storecachedresponse(__for_)-8uq91.md>) — Stores a cached URL response for a specified data task.
