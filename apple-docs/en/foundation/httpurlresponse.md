---
title: HTTPURLResponse
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpurlresponse
source_url: 'https://developer.apple.com/documentation/foundation/httpurlresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpurlresponse.json'
content_hash: 'sha256:428cbea9e9f05fa4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# HTTPURLResponse

<sub>Class</sub>

The metadata associated with the response to an HTTP protocol URL load request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class HTTPURLResponse
```

## Overview

The [HTTPURLResponse](httpurlresponse.md) class is a subclass of [URLResponse](urlresponse.md) that provides methods for accessing information specific to HTTP protocol responses. Whenever you make HTTP URL load requests, any response objects you get back from the [URLSession](urlsession.md), [NSURLConnection](nsurlconnection.md), or [NSURLDownload](nsurldownload.md) class are instances of the [HTTPURLResponse](httpurlresponse.md) class.

## Relationships

- **Inherits From**: [URLResponse](urlresponse.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a response object

- [- initWithURL:statusCode:HTTPVersion:headerFields:](<httpurlresponse/init(url_statuscode_httpversion_headerfields_)-21j4x.md>) — Initializes an HTTP URL response object with a status code, protocol version, and response headers.

### Getting HTTP response headers

- [allHeaderFields](httpurlresponse/allheaderfields.md) — All HTTP header fields of the response.
- [- valueForHTTPHeaderField:](<httpurlresponse/value(forhttpheaderfield_).md>) — Returns the value that corresponds to the given header field.

### Getting response status codes

- [+ localizedStringForStatusCode:](<httpurlresponse/localizedstring(forstatuscode_).md>) — Returns a localized string corresponding to a specified HTTP status code.
- [statusCode](httpurlresponse/statuscode.md) — The response’s HTTP status code.

### Initializers

- [init(URL:statusCode:HTTPVersion:headerFields:)](<httpurlresponse/init(url_statuscode_httpversion_headerfields_)-3kiww.md>)

## See Also

### Requests and responses

- [URLRequest](urlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [NSURLRequest](nsurlrequest.md) — A URL load request that is independent of protocol or URL scheme.
- [NSMutableURLRequest](nsmutableurlrequest.md) — A mutable URL load request that is independent of protocol or URL scheme.
- [URLResponse](urlresponse.md) — The metadata associated with the response to a URL load request, independent of protocol and URL scheme.
