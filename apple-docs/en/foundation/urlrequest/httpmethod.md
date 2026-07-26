---
title: httpMethod
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/httpmethod
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/httpmethod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/httpmethod.json'
content_hash: 'sha256:27bd4dddf6688b33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# httpMethod

<sub>Instance Property</sub>

The HTTP request method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpMethod: String? { get set }
```

## Discussion

The default HTTP method is “GET”.

## See Also

### Accessing request components

- [url](url.md) — The URL of the request.
- [httpBody](httpbody.md) — The data sent as the message body of a request, such as for an HTTP POST request.
- [httpBodyStream](httpbodystream.md) — The stream used to deliver the HTTP body.
- [mainDocumentURL](maindocumenturl.md) — The main document URL associated with this request.
