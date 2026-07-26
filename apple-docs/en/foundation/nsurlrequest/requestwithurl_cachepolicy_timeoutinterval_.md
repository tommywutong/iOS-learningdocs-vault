---
title: 'requestWithURL:cachePolicy:timeoutInterval:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlrequest/requestwithurl:cachepolicy:timeoutinterval:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/requestwithurl:cachepolicy:timeoutinterval:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/requestwithurl%3Acachepolicy%3Atimeoutinterval%3A.json'
content_hash: 'sha256:c56d83089e17f23b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# requestWithURL:cachePolicy:timeoutInterval:

<sub>Type Method</sub>

Creates and returns an initialized URL request with specified URL, cache policy, and timeout values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) requestWithURL:(NSURL *) URL cachePolicy:(NSURLRequestCachePolicy) cachePolicy timeoutInterval:(NSTimeInterval) timeoutInterval;
```

## Parameters

- `URL` — The URL for the new request.

- `cachePolicy` — The cache policy for the new request.

- `timeoutInterval` — The timeout interval for the new request, in seconds.

## Return Value

The initialized URL request.

## See Also

### Creating requests

- [requestWithURL:](requestwithurl_.md) — Creates and returns a URL request for a specified URL.
- [- initWithURL:](<init(url_)-7dmpd.md>) — Creates a URL request for a specified URL.
- [- initWithURL:cachePolicy:timeoutInterval:](<init(url_cachepolicy_timeoutinterval_)-2giyj.md>) — Creates a URL request with the specified URL, cache policy, and timeout values.
