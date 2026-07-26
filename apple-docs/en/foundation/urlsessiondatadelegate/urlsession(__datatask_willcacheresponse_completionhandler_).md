---
title: 'urlSession(_:dataTask:willCacheResponse:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:willcacheresponse:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:willcacheresponse:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondatadelegate/urlsession%28_%3Adatatask%3Awillcacheresponse%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:24b4fd509eaac8cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDataDelegate](../urlsessiondatadelegate.md)

# urlSession(_:dataTask:willCacheResponse:completionHandler:)

<sub>Instance Method</sub>

Asks the delegate whether the data (or upload) task should store the response in the cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, willCacheResponse proposedResponse: CachedURLResponse, completionHandler: @escaping @Sendable (CachedURLResponse?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, willCacheResponse proposedResponse: CachedURLResponse) async -> CachedURLResponse?
```

## Parameters

- `session` — The session containing the data (or upload) task.

- `dataTask` — The data (or upload) task.

- `proposedResponse` — The default caching behavior. This behavior is determined based on the current caching policy and the values of certain received headers, such as the `Pragma` and `Cache-Control` headers.

- `completionHandler` — A block that your handler must call, providing either the original proposed response, a modified version of that response, or `NULL` to prevent caching the response. If your delegate implements this method, it _must_ call this completion handler; otherwise, your app leaks memory.

## Discussion

The session calls this delegate method after the task finishes receiving all of the expected data. If you don’t implement this method, the default behavior is to use the caching policy specified in the session’s configuration object. The primary purpose of this method is to prevent caching of specific URLs or to modify the `userInfo` dictionary associated with the URL response.

This method is called only if the [URLProtocol](../urlprotocol.md) handling the request decides to cache the response. As a rule, responses are cached only when all of the following are true:

- The request is for an HTTP or HTTPS URL (or your own custom networking protocol that supports caching).
- The request was successful (with a status code in the `200–299` range).
- The provided response came from the server, rather than out of the cache.
- The session configuration’s cache policy allows caching.
- The provided [URLRequest](../urlrequest.md) object’s cache policy (if applicable) allows caching.
- The cache-related headers in the server’s response (if present) allow caching.
- The response size is small enough to reasonably fit within the cache. (For example, if you provide a disk cache, the response must be no larger than about 5% of the disk cache size.)
