---
title: mainDocumentURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/maindocumenturl
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/maindocumenturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/maindocumenturl.json'
content_hash: 'sha256:c2979237e4b1738e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# mainDocumentURL

<sub>Instance Property</sub>

The main document URL associated with the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mainDocumentURL: URL? { get }
```

## Discussion

This URL is used for the cookie “same domain as main document” policy.

## See Also

### Related Documentation

- [mainDocumentURL](../nsmutableurlrequest/maindocumenturl.md) — The main document URL.

### Accessing request components

- [HTTPMethod](httpmethod.md) — The HTTP request method.
- [URL](url.md) — The URL being requested.
- [HTTPBody](httpbody.md) — The request body.
- [HTTPBodyStream](httpbodystream.md) — The request body as an input stream.
