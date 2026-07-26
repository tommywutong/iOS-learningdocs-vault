---
title: mainDocumentURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/maindocumenturl
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/maindocumenturl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/maindocumenturl.json'
content_hash: 'sha256:cece6df03c5e7858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# mainDocumentURL

<sub>Instance Property</sub>

The main document URL associated with this request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mainDocumentURL: URL? { get set }
```

## Discussion

This URL is used for the cookie “same domain as main document” policy.

## See Also

### Accessing request components

- [httpMethod](httpmethod.md) — The HTTP request method.
- [url](url.md) — The URL of the request.
- [httpBody](httpbody.md) — The data sent as the message body of a request, such as for an HTTP POST request.
- [httpBodyStream](httpbodystream.md) — The stream used to deliver the HTTP body.
