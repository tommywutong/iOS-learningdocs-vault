---
title: 'requestHeaderFields(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookie/requestheaderfields(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/requestheaderfields(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/requestheaderfields%28with%3A%29.json'
content_hash: 'sha256:120574ac3d1a19f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# requestHeaderFields(with:)

<sub>Type Method</sub>

Converts an array of cookies to a dictionary of header fields.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func requestHeaderFields(with cookies: [HTTPCookie]) -> [String : String]
```

## Parameters

- `cookies` — The cookies from which the header fields are created.

## Return Value

The dictionary of header fields created from the provided cookies.

## Discussion

To send these headers as part of a URL request to a remote server, create an [NSMutableURLRequest](../nsmutableurlrequest.md) object, then call the [allHTTPHeaderFields](../nsmutableurlrequest/allhttpheaderfields.md) or [- setValue:forHTTPHeaderField:](<../nsmutableurlrequest/setvalue(__forhttpheaderfield_).md>) method to set the provided headers for the request. Finally, initialize and start an [URLSessionTask](../urlsessiontask.md) instance based on that request object.
