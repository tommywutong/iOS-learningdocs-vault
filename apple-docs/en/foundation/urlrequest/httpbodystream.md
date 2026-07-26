---
title: httpBodyStream
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/httpbodystream
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/httpbodystream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/httpbodystream.json'
content_hash: 'sha256:38e92bdeed9e69d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# httpBodyStream

<sub>Instance Property</sub>

The stream used to deliver the HTTP body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpBodyStream: InputStream? { get set }
```

## Discussion

The stream is returned for examination only; it’s unsafe for the caller to manipulate the stream in any way.

> [!note] Note
> The [httpBodyStream](httpbodystream.md) and [httpBody](httpbody.md) are mutually exclusive - only one can be set on a given request. The body stream is preserved across copies, but is lost when the request is coded via the [NSCoding](../nscoding.md) protocol

## See Also

### Accessing request components

- [httpMethod](httpmethod.md) — The HTTP request method.
- [url](url.md) — The URL of the request.
- [httpBody](httpbody.md) — The data sent as the message body of a request, such as for an HTTP POST request.
- [mainDocumentURL](maindocumenturl.md) — The main document URL associated with this request.
