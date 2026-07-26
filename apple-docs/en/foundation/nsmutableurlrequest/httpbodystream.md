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
doc_path: /documentation/foundation/nsmutableurlrequest/httpbodystream
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpbodystream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/httpbodystream.json'
content_hash: 'sha256:a7adfdbd8fdab9c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# httpBodyStream

<sub>Instance Property</sub>

The request body as an input stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpBodyStream: InputStream? { get set }
```

## Discussion

The request body of the receiver will be this input stream. The entire contents of the stream will be sent as the body, as in an HTTP `POST` request. The input stream should be unopened and the receiver will take over as the stream’s delegate.

Setting a body stream clears any data in [HTTPBody](httpbody.md). These values are mutually exclusive.

## See Also

### Accessing request components

- [HTTPMethod](httpmethod.md) — The HTTP request method.
- [URL](url.md) — The URL being requested.
- [HTTPBody](httpbody.md) — The request body.
- [mainDocumentURL](maindocumenturl.md) — The main document URL.
