---
title: 'removeCachedResponses(since:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/removecachedresponses(since:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/removecachedresponses(since:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/removecachedresponses%28since%3A%29.json'
content_hash: 'sha256:9b64129e6834f571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# removeCachedResponses(since:)

<sub>Instance Method</sub>

Clears the given cache of any cached responses since the provided date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeCachedResponses(since date: Date)
```

## Parameters

- `date` — The earliest date of responses that should remain in the cache. Any responses with dates later than this parameter should be removed.

## See Also

### Removing cached objects

- [- removeCachedResponseForRequest:](<removecachedresponse(for_)-1dh89.md>) — Removes the cached URL response for a specified URL request.
- [- removeCachedResponseForDataTask:](<removecachedresponse(for_)-1zwp6.md>) — Removes the cached URL response for a specified data task.
- [- removeAllCachedResponses](<removeallcachedresponses().md>) — Clears the receiver’s cache, removing all stored cached URL responses.
