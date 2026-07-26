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
doc_path: /documentation/foundation/nsmutableurlrequest/httpbody
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpbody'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/httpbody.json'
content_hash: 'sha256:484876ecc8d8ff47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# httpBody

<sub>Instance Property</sub>

The request body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpBody: Data? { get set }
```

## Discussion

The request body is sent as the message body of the request, as in an HTTP `POST` request. Setting the HTTP body data clears any input stream in [HTTPBodyStream](httpbodystream.md). These values are mutually exclusive.

## See Also

### Accessing request components

- [HTTPMethod](httpmethod.md) — The HTTP request method.
- [URL](url.md) — The URL being requested.
- [HTTPBodyStream](httpbodystream.md) — The request body as an input stream.
- [mainDocumentURL](maindocumenturl.md) — The main document URL.
