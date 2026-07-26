---
title: 'removeCachedResponse(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/removecachedresponse(for:)-1zwp6'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/removecachedresponse(for:)-1zwp6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/removecachedresponse%28for%3A%29-1zwp6.json'
content_hash: 'sha256:e2f12c2e5027ca25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# removeCachedResponse(for:)

<sub>Instance Method</sub>

Removes the cached URL response for a specified data task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeCachedResponse(for dataTask: URLSessionDataTask)
```

## Parameters

- `dataTask` — A task whose URL request’s corresponding cached URL response should be removed. If there is no corresponding cached URL response, no action is taken.

## See Also

### Removing cached objects

- [- removeCachedResponseForRequest:](<removecachedresponse(for_)-1dh89.md>) — Removes the cached URL response for a specified URL request.
- [- removeCachedResponsesSinceDate:](<removecachedresponses(since_).md>) — Clears the given cache of any cached responses since the provided date.
- [- removeAllCachedResponses](<removeallcachedresponses().md>) — Clears the receiver’s cache, removing all stored cached URL responses.
