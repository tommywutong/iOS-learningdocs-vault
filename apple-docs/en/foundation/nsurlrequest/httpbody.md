---
title: httpBody
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/httpbody
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/httpbody'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/httpbody.json'
content_hash: 'sha256:cace69fceac83ef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# httpBody

<sub>Instance Property</sub>

The request body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpBody: Data? { get }
```

## Discussion

This data is sent as the message body of a request, as in an HTTP `POST` request.

## See Also

### Related Documentation

- [HTTPBodyStream](../nsmutableurlrequest/httpbodystream.md) — The request body as an input stream.
- [HTTPBody](../nsmutableurlrequest/httpbody.md) — The request body.

### Accessing request components

- [HTTPMethod](httpmethod.md) — The HTTP request method.
- [URL](url.md) — The URL being requested.
- [HTTPBodyStream](httpbodystream.md) — The request body as an input stream.
- [mainDocumentURL](maindocumenturl.md) — The main document URL associated with the request.
