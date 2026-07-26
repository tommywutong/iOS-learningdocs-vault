---
title: 'requestWithURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlrequest/requestwithurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/requestwithurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/requestwithurl%3A.json'
content_hash: 'sha256:1adb452fac864a0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# requestWithURL:

<sub>Type Method</sub>

Creates and returns a URL request for a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) requestWithURL:(NSURL *) URL;
```

## Parameters

- `URL` — The URL for the new request.

## Return Value

The newly created URL request.

## Discussion

The request is created with the with the default cache policy ([NSURLRequestUseProtocolCachePolicy](cachepolicy-swift.enum/useprotocolcachepolicy.md)), and the default timeout interval (60 seconds).

## See Also

### Creating requests

- [- initWithURL:](<init(url_)-7dmpd.md>) — Creates a URL request for a specified URL.
- [requestWithURL:cachePolicy:timeoutInterval:](requestwithurl_cachepolicy_timeoutinterval_.md) — Creates and returns an initialized URL request with specified URL, cache policy, and timeout values.
- [- initWithURL:cachePolicy:timeoutInterval:](<init(url_cachepolicy_timeoutinterval_)-2giyj.md>) — Creates a URL request with the specified URL, cache policy, and timeout values.
