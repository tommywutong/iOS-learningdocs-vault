---
title: httpBodyStream
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/httpbodystream
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/httpbodystream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/httpbodystream.json'
content_hash: 'sha256:39b9885829c98b7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# httpBodyStream

<sub>Instance Property</sub>

The request body as an input stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpBodyStream: InputStream? { get }
```

## Discussion

`nil` if the body stream has not been set. The returned stream is for examination only—it is not safe to manipulate the stream in any way.

The receiver will have either an HTTP body or an HTTP body stream, only one may be set for a request. A HTTP body stream is preserved when copying an [NSURLRequest](../nsurlrequest.md) object, but is lost when a request is archived using the [NSCoding](../nscoding.md) protocol.

## See Also

### Related Documentation

- [HTTPBodyStream](../nsmutableurlrequest/httpbodystream.md) — The request body as an input stream.
- [HTTPBody](../nsmutableurlrequest/httpbody.md) — The request body.

### Accessing request components

- [HTTPMethod](httpmethod.md) — The HTTP request method.
- [URL](url.md) — The URL being requested.
- [HTTPBody](httpbody.md) — The request body.
- [mainDocumentURL](maindocumenturl.md) — The main document URL associated with the request.
