---
title: 'localizedString(forStatusCode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpurlresponse/localizedstring(forstatuscode:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpurlresponse/localizedstring(forstatuscode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpurlresponse/localizedstring%28forstatuscode%3A%29.json'
content_hash: 'sha256:f5dca128460fa960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPURLResponse](../httpurlresponse.md)

# localizedString(forStatusCode:)

<sub>Type Method</sub>

Returns a localized string corresponding to a specified HTTP status code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedString(forStatusCode statusCode: Int) -> String
```

## Parameters

- `statusCode` — The HTTP status code. See [RFC 2616](http://www.ietf.org/rfc/rfc2616.txt) for details.

## Return Value

A localized string suitable for displaying to users that describes the specified status code.

## See Also

### Getting response status codes

- [statusCode](statuscode.md) — The response’s HTTP status code.
