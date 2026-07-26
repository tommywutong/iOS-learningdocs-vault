---
title: httpMethod
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/httpmethod
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/httpmethod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/httpmethod.json'
content_hash: 'sha256:1327c9435024fcf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# httpMethod

<sub>Instance Property</sub>

The HTTP request method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpMethod: String? { get }
```

## Discussion

The default HTTP method is “GET”.

## See Also

### Related Documentation

- [HTTPMethod](../nsmutableurlrequest/httpmethod.md) — The HTTP request method.

### Accessing request components

- [URL](url.md) — The URL being requested.
- [HTTPBody](httpbody.md) — The request body.
- [HTTPBodyStream](httpbodystream.md) — The request body as an input stream.
- [mainDocumentURL](maindocumenturl.md) — The main document URL associated with the request.
