---
title: 'cachedResponse(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/cachedresponse(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/cachedresponse(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/cachedresponse%28for%3A%29.json'
content_hash: 'sha256:7131140d053f0053'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# cachedResponse(for:)

<sub>Instance Method</sub>

Returns the cached URL response in the cache for the specified URL request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cachedResponse(for request: URLRequest) -> CachedURLResponse?
```

## Parameters

- `request` — The URL request whose cached response is desired.

## Return Value

The cached URL response for `request`, or `nil` if no response has been cached.

## Discussion

If you override this method, you should also override [- getCachedResponseForDataTask:completionHandler:](<getcachedresponse(for_completionhandler_).md>).

## See Also

### Getting and storing cached objects

- [- storeCachedResponse:forRequest:](<storecachedresponse(__for_)-7p7bl.md>) — Stores a cached URL response for a specified request.
- [- getCachedResponseForDataTask:completionHandler:](<getcachedresponse(for_completionhandler_).md>) — Gets the cached URL response for a data task, passing it to the provided completion handler.
- [- storeCachedResponse:forDataTask:](<storecachedresponse(__for_)-8uq91.md>) — Stores a cached URL response for a specified data task.
