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
doc_path: /documentation/foundation/nsmutableurlrequest/maindocumenturl
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/maindocumenturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/maindocumenturl.json'
content_hash: 'sha256:cab498335650dfef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# mainDocumentURL

<sub>Instance Property</sub>

The main document URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mainDocumentURL: URL? { get set }
```

## Discussion

The caller should set the main document URL to an appropriate main document, if known. For example, when loading a web page the URL of the HTML document for the top-level frame would be appropriate. This URL will be used for the “only from same domain as main document” cookie accept policy.

`nil` indicates no main document.

## See Also

### Accessing request components

- [HTTPMethod](httpmethod.md) — The HTTP request method.
- [URL](url.md) — The URL being requested.
- [HTTPBody](httpbody.md) — The request body.
- [HTTPBodyStream](httpbodystream.md) — The request body as an input stream.
