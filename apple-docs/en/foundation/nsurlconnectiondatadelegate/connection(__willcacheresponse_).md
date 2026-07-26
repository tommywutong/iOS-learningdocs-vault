---
title: 'connection(_:willCacheResponse:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondatadelegate/connection(_:willcacheresponse:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:willcacheresponse:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondatadelegate/connection%28_%3Awillcacheresponse%3A%29.json'
content_hash: 'sha256:9f51d3a2f28de77c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDataDelegate](../nsurlconnectiondatadelegate.md)

# connection(_:willCacheResponse:)

<sub>Instance Method</sub>

Sent before the connection stores a cached response in the cache, to give the delegate an opportunity to alter it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, willCacheResponse cachedResponse: CachedURLResponse) -> CachedURLResponse?
```

## Parameters

- `connection` — The connection sending the message.

- `cachedResponse` — The proposed cached response to store in the cache.

## Return Value

The actual cached response to store in the cache. The delegate may return `cachedResponse` unmodified, return a modified cached response, or return `nil` if no cached response should be stored for the connection.

## Discussion

This method is called only if the [URLProtocol](../urlprotocol.md) handling the request decides to cache the response. As a rule, responses are cached only when all of the following are true:

- The request is for an HTTP or HTTPS URL (or your own custom networking protocol that supports caching).
- The request was successful (with a status code in the `200–299` range).
- The provided response came from the server, rather than out of the cache.
- The [NSURLRequest](../nsurlrequest.md) object’s cache policy allows caching.
- The cache-related headers in the server’s response (if present) allow caching.
- The response size is small enough to reasonably fit within the cache. (For example, if you provide a disk cache, the response must be no larger than about 5% of the disk cache size.)
