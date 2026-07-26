---
title: statusCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpurlresponse/statuscode
source_url: 'https://developer.apple.com/documentation/foundation/httpurlresponse/statuscode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpurlresponse/statuscode.json'
content_hash: 'sha256:9e1b58766359bed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPURLResponse](../httpurlresponse.md)

# statusCode

<sub>Instance Property</sub>

The response’s HTTP status code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var statusCode: Int { get }
```

## Discussion

See [RFC 2616](http://www.ietf.org/rfc/rfc2616.txt) for details.

## See Also

### Getting response status codes

- [+ localizedStringForStatusCode:](<localizedstring(forstatuscode_).md>) — Returns a localized string corresponding to a specified HTTP status code.
