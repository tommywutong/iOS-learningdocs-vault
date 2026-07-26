---
title: 'getCachedResponse(for:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/getcachedresponse(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/getcachedresponse(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/getcachedresponse%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3656156ca85bb4af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# getCachedResponse(for:completionHandler:)

<sub>Instance Method</sub>

Gets the cached URL response for a data task, passing it to the provided completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCachedResponse(for dataTask: URLSessionDataTask, completionHandler: @escaping @Sendable (CachedURLResponse?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cachedResponse(for dataTask: URLSessionDataTask) async -> CachedURLResponse?
```

## Parameters

- `dataTask` — The data task whose cached URL response is desired.

- `completionHandler` — A completion handler that receives the cached URL response for the data task’s request, or `nil` if no response is found in the cache.

## See Also

### Getting and storing cached objects

- [- cachedResponseForRequest:](<cachedresponse(for_).md>) — Returns the cached URL response in the cache for the specified URL request.
- [- storeCachedResponse:forRequest:](<storecachedresponse(__for_)-7p7bl.md>) — Stores a cached URL response for a specified request.
- [- storeCachedResponse:forDataTask:](<storecachedresponse(__for_)-8uq91.md>) — Stores a cached URL response for a specified data task.
