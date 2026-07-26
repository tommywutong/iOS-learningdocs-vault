---
title: 'init(url:cachePolicy:timeoutInterval:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlrequest/init(url:cachepolicy:timeoutinterval:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/init(url:cachepolicy:timeoutinterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/init%28url%3Acachepolicy%3Atimeoutinterval%3A%29.json'
content_hash: 'sha256:3ac7d24d54b6c40e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# init(url:cachePolicy:timeoutInterval:)

<sub>Initializer</sub>

Creates and initializes a URL request with the given URL, cache policy, and timeout interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(url: URL, cachePolicy: URLRequest.CachePolicy = .useProtocolCachePolicy, timeoutInterval: TimeInterval = 60.0)
```

## Parameters

- `url` — The URL for the request.

- `cachePolicy` — The cache policy for the request. The default is [NSURLRequestUseProtocolCachePolicy](../nsurlrequest/cachepolicy-swift.enum/useprotocolcachepolicy.md).

- `timeoutInterval` — The timeout interval for the request. The default is `60.0`. See the commentary for the [timeoutInterval](../nsurlrequest/timeoutinterval.md) for more information on timeout intervals.
