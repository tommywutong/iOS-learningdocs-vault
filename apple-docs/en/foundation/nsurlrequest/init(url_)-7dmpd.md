---
title: 'init(url:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlrequest/init(url:)-7dmpd'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/init(url:)-7dmpd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/init%28url%3A%29-7dmpd.json'
content_hash: 'sha256:8833688f28d79def'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# init(url:)

<sub>Initializer</sub>

Creates a URL request for a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(url URL: URL)
```

## Parameters

- `URL` — The URL for the request.

## Return Value

The initialized URL request.

## Discussion

The request is created with the with the default cache policy ([NSURLRequestUseProtocolCachePolicy](cachepolicy-swift.enum/useprotocolcachepolicy.md)), and the default timeout interval (60 seconds).

## See Also

### Creating requests

- [- initWithURL:cachePolicy:timeoutInterval:](<init(url_cachepolicy_timeoutinterval_)-2giyj.md>) — Creates a URL request with the specified URL, cache policy, and timeout values.
