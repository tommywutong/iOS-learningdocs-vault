---
title: 'removeCachedResponse(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcache/removecachedresponse(for:)-1dh89'
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/removecachedresponse(for:)-1dh89'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/removecachedresponse%28for%3A%29-1dh89.json'
content_hash: 'sha256:3a9665dab9808a3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# removeCachedResponse(for:)

<sub>Instance Method</sub>

Removes the cached URL response for a specified URL request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeCachedResponse(for request: URLRequest)
```

## Parameters

- `request` — The URL request whose cached URL response should be removed. If there is no corresponding cached URL response, no action is taken.

## Discussion

If you override this method, you should also override [- removeCachedResponseForDataTask:](<removecachedresponse(for_)-1zwp6.md>).

## See Also

### Removing cached objects

- [- removeCachedResponseForDataTask:](<removecachedresponse(for_)-1zwp6.md>) — Removes the cached URL response for a specified data task.
- [- removeCachedResponsesSinceDate:](<removecachedresponses(since_).md>) — Clears the given cache of any cached responses since the provided date.
- [- removeAllCachedResponses](<removeallcachedresponses().md>) — Clears the receiver’s cache, removing all stored cached URL responses.
