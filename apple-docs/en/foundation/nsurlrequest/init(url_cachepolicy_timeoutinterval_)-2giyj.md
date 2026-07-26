---
title: 'init(url:cachePolicy:timeoutInterval:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlrequest/init(url:cachepolicy:timeoutinterval:)-2giyj'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/init(url:cachepolicy:timeoutinterval:)-2giyj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/init%28url%3Acachepolicy%3Atimeoutinterval%3A%29-2giyj.json'
content_hash: 'sha256:fde555349b6ff090'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# init(url:cachePolicy:timeoutInterval:)

<sub>Initializer</sub>

Creates a URL request with the specified URL, cache policy, and timeout values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(url URL: URL, cachePolicy: NSURLRequest.CachePolicy, timeoutInterval: TimeInterval)
```

## Parameters

- `URL` — The URL for the request.

- `cachePolicy` — The cache policy for the request.

- `timeoutInterval` — The timeout interval for the request, in seconds.

## Return Value

The initialized URL request.

## Discussion

This is the designated initializer for `NSURLRequest`.

## See Also

### Creating requests

- [- initWithURL:](<init(url_)-7dmpd.md>) — Creates a URL request for a specified URL.
