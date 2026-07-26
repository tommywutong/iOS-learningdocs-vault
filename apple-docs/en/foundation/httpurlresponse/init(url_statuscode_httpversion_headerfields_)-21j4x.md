---
title: 'init(url:statusCode:httpVersion:headerFields:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpurlresponse/init(url:statuscode:httpversion:headerfields:)-21j4x'
source_url: 'https://developer.apple.com/documentation/foundation/httpurlresponse/init(url:statuscode:httpversion:headerfields:)-21j4x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpurlresponse/init%28url%3Astatuscode%3Ahttpversion%3Aheaderfields%3A%29-21j4x.json'
content_hash: 'sha256:f69cf8e6dde42874'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPURLResponse](../httpurlresponse.md)

# init(url:statusCode:httpVersion:headerFields:)

<sub>Initializer</sub>

Initializes an HTTP URL response object with a status code, protocol version, and response headers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(url: URL, statusCode: Int, httpVersion HTTPVersion: String?, headerFields: [String : String]?)
```

## Parameters

- `url` — The URL from which the response was generated.

- `statusCode` — The HTTP status code to return (`404`, for example). See [RFC 2616](http://www.ietf.org/rfc/rfc2616.txt) for details.

- `HTTPVersion` — The version of the HTTP response as returned by the server. This is typically represented as “HTTP/1.1”.

- `headerFields` — A dictionary representing the keys and values from the server’s response header.

## Return Value

An initialized [HTTPURLResponse](../httpurlresponse.md) object or `nil` if an error occurred during initialization.
