---
title: httpBody
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/httpbody
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/httpbody'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/httpbody.json'
content_hash: 'sha256:b403e062e413045e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# httpBody

<sub>Instance Property</sub>

The data sent as the message body of a request, such as for an HTTP POST request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpBody: Data? { get set }
```

## See Also

### Accessing request components

- [httpMethod](httpmethod.md) — The HTTP request method.
- [url](url.md) — The URL of the request.
- [httpBodyStream](httpbodystream.md) — The stream used to deliver the HTTP body.
- [mainDocumentURL](maindocumenturl.md) — The main document URL associated with this request.
